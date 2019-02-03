import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {NavigationComponent} from './navigation/navigation.component';
import {RouterModule, Routes} from '@angular/router';
import {
  MatButtonModule,
  MatIconModule,
  MatListModule,
  MatNativeDateModule,
  MatSidenavModule,
  MatToolbarModule,
} from '@angular/material';
import {CommonModule} from '@angular/common';
import {AccountComponent} from './account/account.component';
import {TasksComponent} from './tasks/tasks.component';
import {HomeComponent} from './home/home.component';
import {HttpClientModule} from '@angular/common/http';

const appRoutes: Routes = [
  {path: '', component: HomeComponent, data: {title: 'Home'}},
  {path: 'my_account', component: AccountComponent, data: {title: 'My Account'}},
  {path: 'tasks', component: TasksComponent, data: {title: 'Tasks'}}
];

@NgModule({
  declarations: [
    AppComponent,
    NavigationComponent,
    AccountComponent,
    TasksComponent,
    HomeComponent
  ],
  imports: [
    CommonModule,
    HttpClientModule,
    MatButtonModule,
    MatToolbarModule,
    MatNativeDateModule,
    MatIconModule,
    MatSidenavModule,
    MatListModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(
      appRoutes,
      {useHash: true}
    ),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
