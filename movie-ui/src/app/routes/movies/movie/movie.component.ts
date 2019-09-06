import { Component, OnInit } from '@angular/core';
import { Movie } from '../movie';
import { Constants } from '../../../config/Constant';
import { Service } from '../../../app.service';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router'
import 'rxjs/add/operator/filter';

@Component({
  selector: 'app-movie',
  templateUrl: './movie.component.html',
  styleUrls: ['./movie.component.scss']
})
export class MovieComponent implements OnInit {

  constructor(private router: Router, private route: ActivatedRoute, private service: Service) { }


  movieDetails: Movie = {

    Title: "",
    Year: "",
    Rated: "",
    Released: "",
    Runtime: "",
    Genre: "",
    Director: "",
    Writer: "",
    Actors: "",
    Plot: "",
    Language: "",
    Country: "",
    Awards: "",
    Poster: "",
    Ratings: [],
    Metascore: "",
    imdbRating: "",
    imdbVotes: "",
    imdbID: "",
    Type: "",
    DVD: "",
    BoxOffice: "",
    Production: "",
    Website: "",
    Response: ""

  };

  movieOperation = "add";

  movieRatings = {
    Source: "",
    Value: ""
  }
  movieRatingsArr: Array<any> = [];

  ngOnInit() {
    this.route.queryParams.filter(params => params.id)
      .subscribe(params => {
        if (params.id) {
          this.movieOperation = "edit"
          this.getMovieById(params.id);
        }
      });
  }

  getMovieById(movie_id) {
    const url = `${Constants.getMoviesById}${movie_id}`;
    this.service.get(url)
      .subscribe(data => {
        this.movieDetails = data;
      }, error => {
        console.error('error:', error);
      });
  }

  addMovie() {

    this.movieDetails.Ratings.push(this.movieRatings);
    // this.movieDetails.Ratings = this.movieRatingsArr;
    const url = `${Constants.addMovie}`;
    this.service.post(url, this.movieDetails)
      .subscribe(data => {
        this.router.navigate(['/movie/list'])
      }, error => {
        console.error('error:', error);
      });

  }

  updateMovie(movie_id) {

    const url = `${Constants.updateMovie}${movie_id}`;
    this.service.put(url, this.movieDetails)
      .subscribe(data => {
        this.router.navigate(['/movie/list'])
      }, error => {
        console.error('error:', error);
      });

  }

}
