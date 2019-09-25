import { NgModule }             from '@angular/core';
import { BrowserModule }        from '@angular/platform-browser';
import { FormsModule }          from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent }          from './app.component';
import { HomeComponent }         from './home/home.component';
import { LeaderboardComponent }         from './leaderboard/leaderboard.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'leaderboard', component: LeaderboardComponent },
  { path: '**', component: PageNotFoundComponent }
];

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    )
  ],
  declarations: [
    AppComponent,
    HomeComponent,
    LeaderboardComponent,
    PageNotFoundComponent
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
