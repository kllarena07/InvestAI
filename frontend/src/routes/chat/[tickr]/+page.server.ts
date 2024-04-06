import type { PageServerLoad } from '../$types';
import type { Actions } from '@sveltejs/kit';

export const actions = {
	default: async ({ request }) => {}
} satisfies Actions;

export const load: PageServerLoad = ({ params }) => {
	return {
		tickr: params.tickr
	};
};
