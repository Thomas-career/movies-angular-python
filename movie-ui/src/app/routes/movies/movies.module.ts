import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SharedModule } from '../../shared/shared.module';

import { MovielistComponent } from './movielist/movielist.component';
import { MoviedetailsComponent } from './moviedetails/moviedetails.component';
import { MovieComponent } from './movie/movie.component'
import { InfiniteScrollModule } from 'ngx-infinite-scroll';

import { AuthGuard } from '../../app.auth-guard';

const routes: Routes = [


    { path: '', redirectTo: 'list', pathMatch: 'full' },

    { path: 'list', component: MovielistComponent },
    { path: 'details', component: MoviedetailsComponent },
    { path: 'edit', component: MovieComponent, canActivate: [AuthGuard] },
    { path: 'add', component: MovieComponent, canActivate: [AuthGuard] }

];

@NgModule({
    imports: [
        SharedModule,
        RouterModule.forChild(routes),
        InfiniteScrollModule
    ],
    declarations: [
        MovielistComponent,
        MoviedetailsComponent,
        MovieComponent
    ],
    exports: [
        RouterModule
    ]
})
export class MoviesModule { }

