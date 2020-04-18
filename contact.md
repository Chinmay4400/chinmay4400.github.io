---
layout: page
title: Contact Me
image: assets/images/pic11.jpg
nav-menu: true
---
<!-- Contact -->
<section id="contact">
	<div class="inner">
		<section>
			<header class="major">
				<h2>Contact Me</h2>
			</header>
			<p>Would like to connect? Feel free to contact me.<br>I'll respond as soon as possible.</p>
			<form action="https://formspree.io/{{ site.email }}" method="POST">
				<div class="field half first">
					<label for="name">Name</label>
					<input type="text" name="name" id="name" />
				</div>
				<div class="field half">
					<label for="email">Email</label>
					<input type="text" name="_replyto" id="email" />
				</div>
				<div class="field">
					<label for="message">Message</label>
					<textarea name="message" id="message" rows="6"></textarea>
				</div>
				<ul class="actions">
					<li><input type="submit" value="Send Message" class="special" /></li>
					<li><input type="reset" value="Clear" /></li>
				</ul>
			</form>
		</section>
	</div>
</section>