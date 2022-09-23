import router from '@/router'

const authGuard = function () {

    let token = localStorage.getItem('connecter')
    console.log(token);
    
    if (token==null) {

        router.push('/Connexion')

    }

    
    // else {
    //     router.push('/Connexion');
    //     localStorage.setItem('token', 'payement');
    // }
    // else {
    //     localStorage.setItem('token', 'payement');
    // }

}

const accueilGuard = function() {
    let page = localStorage.getItem('page')

    console.log(page)

    // if (token=="payement") {
    //     router.push("/payement");
    //     localStorage.setItem('token', '');
    // }
    
}

export {
    authGuard,
    accueilGuard
}