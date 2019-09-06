import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'

import { Constants } from '../../../config/Constant';
import { Service } from '../../../app.service';
// import movieData from '../../../shared/movies.json';
import { Movie } from '../movie';

@Component({
    selector: 'app-movielist',
    templateUrl: './movielist.component.html',
    styleUrls: ['./movielist.component.scss']
})
export class MovielistComponent implements OnInit {



    public movieList: Movie[] = [];

    public currentPage: number = 1;

    public currentUser = JSON.parse(localStorage.getItem('currentUser'));

    constructor(private router: Router, private service: Service) { }

    ngOnInit() {
        this.getAllMovies();
    }

    gotoDetails(movie_id) {
        this.router.navigate(['/movie/details'], { queryParams: { id: movie_id } });
    }

    getAllMovies() {
        const url = `${Constants.getMoviesPaginate}${this.currentPage}`;
        this.service.get(url)
            .subscribe(data => {           
                data.forEach(element => {
                    this.movieList.push(element);
                });
            }, error => {
                console.error('error:', error);
            });
    }

    onScrollDown() {
        console.log('scrolled down!!');

        this.currentPage += 1;
        this.getAllMovies();
 
    }



}
