import Movie from './components/Movie.vue';
import Order from './components/Order.vue';

export const routes = [
  {
    path:'/movies',
    component: Movie
  },
  {
    path: '/order/',
    component: Order,
  },

];

