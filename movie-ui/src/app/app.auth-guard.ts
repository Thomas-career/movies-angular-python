import { Injectable } from '@angular/core';
import { Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

@Injectable()
export class AuthGuard {

    constructor(private router: Router) { }

    async canActivate() {
        const currentUser = await localStorage.getItem('currentUser');
        if (currentUser) {
            return true;
        }
        else {
            // not logged in so redirect to login page with the return url
            this.router.navigate(['/login']);
        }
    }
}