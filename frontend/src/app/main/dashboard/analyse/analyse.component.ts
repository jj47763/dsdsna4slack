import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Archive } from '../../../model/archive';
import { Channel } from '../../../model/channel';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';

@Component({
  selector: 'app-analyse',
  templateUrl: './analyse.component.html',
  styleUrls: ['./analyse.component.css']
})
export class AnalyseComponent implements OnInit {
  loading: boolean;
  archives: Observable<Array<Archive>>; 

  archivesArray: Array<Archive>;
  archivesSubject: BehaviorSubject<Array<Archive>>;

  channelsArray: Array<Channel>;
  channelsSubject: BehaviorSubject<Array<Channel>>;

  selectedArchive: number;
  selectedGraphType: number;

  graphTypes: Array<any> = [{id:0, name:'mention based.'}, {id:1, name:'subscription based.'}];

  channels: Array<any>;

  constructor() { }

  ngOnInit() {
    var tmpArchive: Archive = new Archive();
    tmpArchive.id = 0;
    tmpArchive.name = 'Select your archive';
    
    var tmpArchive2: Archive = new Archive();
    tmpArchive2.id = 1;
    tmpArchive2.name = 'DSD-sna4slack2';
    tmpArchive2.lastModified = new Date(2017, 11, 10, 0,0,0,0);

    this.archivesArray = [tmpArchive, tmpArchive2];
    this.archivesSubject = new BehaviorSubject<Array<Archive>>(this.archivesArray);
    this.archives = this.archivesSubject.asObservable();

    this.selectedArchive = -1;
    this.selectedGraphType = 0;

    this.addChannels();

    this.channelsSubject.subscribe({next: incomingChannels => {
      this.channels = [];
      for(let chan of incomingChannels){
        this.channels.push({checked: false, channel: chan});
        console.log(chan.id);
      }
    }});
  }

  addChannels() {
    this.channelsSubject = new BehaviorSubject<Array<Channel>>([
      new Channel(0, 'all'),
      new Channel(1, 'general'),
      new Channel(2, 'random')
    ]);
  }

  selectArchive(archiveID: string){
    console.log(archiveID);
  }

  selectGraphType(archiveID: string){
    console.log(archiveID);
  }

  analyse() {
    console.log('I\'m analisyng');
  }
}
