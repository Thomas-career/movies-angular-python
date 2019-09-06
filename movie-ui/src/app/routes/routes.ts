import { LayoutComponent } from '../layout/layout.component';

import { LoginComponent } from './pages/login/login.component';
import { RegisterComponent } from './pages/register/register.component';


export const routes = [

    {
        path: '',
        component: LayoutComponent,
        children: [
            { path: '', redirectTo: 'movie', pathMatch: 'full' },
            { path: 'movie', loadChildren: './movies/movies.module#MoviesModule' }
        ]
    },

    // Not lazy-loaded routes
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },

    // Not found
    { path: '**', redirectTo: 'movie' }

];
