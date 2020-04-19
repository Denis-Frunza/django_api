import Movie from './components/Movie.vue';
import Order from './components/Order.vue';
import Login from './components/LoginApp.vue';

export const routes = [
  {
    path:'/movies',
    component: Movie
  },
  {
    path: '/order/:id',
    component: Order,
  },
  {
    path: '/login',
    component: Login,
  },
];

