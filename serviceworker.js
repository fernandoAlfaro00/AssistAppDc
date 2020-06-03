var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
        .then(function(response) {

          return fetch(event.request)
          .catch(function(rsp) {
             return response; 
          });
          
          
        })
    );
});



//codigo para notificaciones push

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyB6HQS3n7iVpUHd5w2llu8ARIPLV1qPTco",
  authDomain: "sistemas-de-solicitud-salas.firebaseapp.com",
  databaseURL: "https://sistemas-de-solicitud-salas.firebaseio.com",
  projectId: "sistemas-de-solicitud-salas",
  storageBucket: "sistemas-de-solicitud-salas.appspot.com",
  messagingSenderId: "1028150775695",
  appId: "1:1028150775695:web:f7f147f0c32555821885fa"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging  = firebase.messaging();



messaging.setBackgroundMessageHandler(function(payload) {

  let title = "titulo de la notificacion";

  let options = {
      body: 'es el mensaje',
      icon: './static/icon/notication.svg'
  }

  self.Registration.showNotification(title ,options);

})


