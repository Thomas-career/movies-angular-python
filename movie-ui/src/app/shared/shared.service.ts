import { Injectable } from '@angular/core';


@Injectable({
    providedIn: 'root'
})
export class SharedService {

    public API_URL: String = 'http://localhost:5000';
}
