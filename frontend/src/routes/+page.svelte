<script>
	import { enhance } from '$app/forms';
	import Button from '$lib/components/ui/button/button.svelte';
	import Input from '$lib/components/ui/input/input.svelte';
</script>

<main class="w-full h-dvh flex justify-center items-center">
	<form method="POST" class="flex flex-col gap-5" action="?/sendTICKR" use:enhance>
		<h1 class="font-bold text-3xl">Enter Company TICKR</h1>
		<Input name="tickr" placeholder="Enter a company TICKR" />
		<Button type="submit">Submit</Button>
	</form>
</main>
