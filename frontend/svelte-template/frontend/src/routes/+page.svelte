<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
</script>

<div class="flex min-h-svh flex-col items-center justify-center gap-4 p-8">
	<h1 class="text-4xl font-bold">Welcome to SvelteKit</h1>
	<p>
		Visit <a class="text-primary underline underline-offset-4" href="https://svelte.dev/docs/kit"
			>svelte.dev/docs/kit</a
		> to read the documentation
	</p>
	<div class="flex flex-wrap gap-2">
		<Button>Default</Button>
		<Button variant="secondary">Secondary</Button>
		<Button variant="outline">Outline</Button>
		<Button variant="ghost">Ghost</Button>
		<Button variant="destructive">Destructive</Button>
		<Button variant="link">Link</Button>
	</div>
</div>
