import type { Actions } from '@sveltejs/kit';

export const actions = {
	sendTICKR: async ({ request }) => {
		const data: FormData = await request.formData();
		const tickr = data.get('tickr');
	}
} satisfies Actions;
