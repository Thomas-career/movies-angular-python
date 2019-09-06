import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class Constants {

    //auth
    public static get userRegister(): String { return '/api/v1/auth/register'; }
    public static get userLogin(): String { return '/api/v1/auth/login'; }


    // movie
    public static get getMoviesPaginate(): String { return '/api/v1/movie/page/'; }
    public static get getMoviesById(): String { return '/api/v1/movie/'; }
    public static get addMovie(): String { return '/api/v1/movie/'; }
    public static get updateMovie(): String { return '/api/v1/movie/'; }
    

}
