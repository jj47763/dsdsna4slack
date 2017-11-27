import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';

import {AppComponent} from './app.component';
import {AlertComponent} from './components/alert/alert.component';
import {HomeComponent} from './main/home/home.component';
import {RegisterComponent} from './main/register/register.component';
import {ArchiveComponent} from './main/dashboard/archive/archive.component';
import {BaseRequestOptions, HttpModule} from "@angular/http";
import {FormsModule} from "@angular/forms";
import {UserService} from "./services/user.service";
import {AuthenticationService} from "./services/authentication.service";
import {AlertService} from "./services/alert.service";
import {AuthGuard} from "./guards/auth.guard";
import {routing} from "./app.routing";
import {DashboardComponent} from './main/dashboard/dashboard.component';
import {AnalyseComponent} from './main/dashboard/analyse/analyse.component';
import {ResultsComponent} from './main/dashboard/results/results.component';
import {ShareComponent} from './main/dashboard/share/share.component';
import {ArchiveService} from "./services/archive.service";

let homeState = {name: 'home', url: '/', component: HomeComponent};
let registerState = {name: 'register', url: '/register', component: RegisterComponent};

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    NgbModule.forRoot(),
    routing
  ],
  declarations: [
    AppComponent,
    AlertComponent,
    HomeComponent,
    RegisterComponent,
    DashboardComponent,
    ArchiveComponent,
    AnalyseComponent,
    ResultsComponent,
    ShareComponent
  ],
  providers: [
    AuthGuard,
    AlertService,
    AuthenticationService,
    UserService,
    ArchiveService,

    BaseRequestOptions
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
