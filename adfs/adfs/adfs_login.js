console.log("adfs login_________")

$(".btn-adfs-login").on("click", function (event) {
	console.log("click___")
	frappe.call({
		freeze:true,
		freeze_message:"Redirectiing to ADFS server ...............",
		method:"adfs.adfs.adfs_login.init_adfs_request",
		callback:function(r){
			console.log(r.message, "in callback")
			console.log("afterdescode____", decodeURIComponent(r.message))
			pop_up_window(r.message,"ADFS Integration");
		}
	})
})



pop_up_window = function(url,windowName) {
      newwindow = window.open(url, windowName, 'height=400,width=600 ,top= 200, left=400');
      if (window.focus){newwindow.focus()}
      return false;
}
