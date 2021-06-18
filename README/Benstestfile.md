Bootstrap defaults:

<!-- This should make the size the same as whatever device it's on, goes above Title -->
<meta name="viewport" content="width - device-width, initial-scale = 1"

<!-- Add in CDN, double check with Mitch. Add in JQuery link -->


<!-- Disabled button for cities -->
<button type="button" class="btn"


Animation for modal box

.animate {
animation: zoom 0.6s
}
@keyframes zoom {
from {transform: scale(0)}
to {transform: scale(1)}
}

---------------------------------

JS

//modal-wrapper is id of div, modal is the class

views file
import UserCreationForm

class Signup(View):
	def get(self, request):
		form = UserCreationForm()
		context = {"form": form}
		return render(request, "signup.html", context)

	def post(self, request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("home")
		else:
			context = {"form": form}
			return render(request, "signup.html", context)


var modal = document.getElementById('modal-wrapper');
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

--------------------------------

	<form id="login-form" action="#" method="post">
		<fieldset>	

			<!-- <legend>Log in</legend> -->
			
			<label for="login">Email</label>
			<input type="text" id="login" name="login"/>
			<div class="clear"></div>
			
			<label for="password">Password</label>
			<input type="password" id="password" name="password"/>
			<div class="clear"></div>
			
			<!-- <label for="remember_me" style="padding: 0;">Remember me?</label>

		    <input type="checkbox" id="remember_me" style="position: relative; top: 3px; margin: 0; " name="remember_me"/> -->

			<div class="clear"></div>
			
			<br />
			
			<input type="submit" style="margin: -20px 0 0 287px;" class="button" name="commit" value="Log in"/>	
		</fieldset>
	</form>


