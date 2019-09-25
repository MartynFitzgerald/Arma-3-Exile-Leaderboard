
	document.title = "Server Stats - Spartan Gaming"

	window.onload = function() {
			var x = document.getElementById("div_info");
			var y = document.getElementById("div_button");
			if (localStorage.getItem("playerName") == null || localStorage.getItem("playerName") == undefined ) {
					x.style.display = "none";
					y.style.display = "block";
			} else {
					x.style.display = "block";
					y.style.display = "none";
			}
		};
		function steam_logout() {
			document.cookie = "_uid=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
			localStorage.removeItem("playerID");
			localStorage.removeItem("playerName");
			localStorage.removeItem("playerURL");
			localStorage.removeItem("playerAvatar");
			localStorage.removeItem("playerAvatarFull");

			x.style.display = "block";
			y.style.display = "none";
		};
