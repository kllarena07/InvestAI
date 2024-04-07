import type { PageServerLoad } from '../$types';
import type { Actions } from '@sveltejs/kit';

export const actions = {
	default: async ({ request }) => {
		const data = await request.formData();
		const response = await fetch('http://127.0.0.1:8000/query/', {
			method: 'POST',
			body: data
		});
		const json = await response.json();

		return {
			llm_response: json.llm_response
		};
	}
} satisfies Actions;

export const load: PageServerLoad = ({ params }) => {
	return {
		tickr: params.tickr
	};
};
