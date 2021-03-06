from rest_framework import serializers

from analysis.models import OverallMetrics
from analysis.utils import create_subscription_graph, calculate_density, calculate_average_path_length, \
    calculate_edge_connectivity, calculate_node_connectivity, create_mention_graph
from archive.serializers import Archive, Channel


class OverallMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverallMetrics
        exclude = ('analysed_channels',)


class ChannelField(serializers.SlugRelatedField):

    def get_queryset(self):
        queryset = Channel.objects.filter(archive__user=self.context['request'].user)
        return queryset


class MakeOverallMetricsSerializer(serializers.ModelSerializer):
    channels = ChannelField(many=True, slug_field='name')

    def validate(self, data):

        if self.context['request'].user != data['archive'].user:
            raise serializers.ValidationError("User is not owner of the archive")

        for channel in data['channels']:
            if channel.archive != data['archive']:
                raise serializers.ValidationError("Channel is not in given archive")

        return data

    class Meta:
        model = OverallMetrics
        fields = ('archive', 'channels', 'graph_type')

    def __init__(self, *args, **kwargs):
        super(MakeOverallMetricsSerializer, self).__init__(*args, **kwargs)

        if self.context.get('request'):
            self.fields['archive'] = serializers.PrimaryKeyRelatedField(
                queryset=Archive.objects.filter(user=self.context['request'].user))

    def check_if_already_exist(self, archive, channels_id, graph_type):
        analysis = OverallMetrics.objects.filter(archive=archive, analysed_channels=channels_id, graph_type=graph_type)
        if analysis:
            return analysis[0]

    def save(self, archive, channels, graph_type):
        channels_id = [channel.id for channel in channels]
        result = self.check_if_already_exist(archive, channels_id, graph_type)
        if result:
            return OverallMetricsSerializer(result).data

        if graph_type == 'subscription':
            graph, dict_graph = create_subscription_graph(archive, channels)
        else:
            graph, dict_graph = create_mention_graph(archive, channels)

        overall_subscription = OverallMetrics.objects.create(
            archive=archive,
            density=calculate_density(graph),
            path_length=calculate_average_path_length(graph),
            node_connectivity=calculate_node_connectivity(graph),
            edge_connectivity=calculate_edge_connectivity(graph),
            json_graph=dict_graph,
            graph_type=graph_type,
            analysed_channels=channels_id
        )

        return OverallMetricsSerializer(overall_subscription).data
