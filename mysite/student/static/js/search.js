var HeaderManager = {
	initialize: function() {
		this.searchDropdown = $("searchDropdown");
		this.searchDropdown.store("visible", false);
		this.searchDropdownToggles = $$(".search-toggle");
		this.searchDropdownToggles.addEvent("click",
		function(a) {
			a.stop();
			if (this.searchDropdown.retrieve("visible")) {
				this.hideSearchDropdown()
			} else {
				this.showSearchDropdown()
			}
		}.bind(this))
	},
	showSearchDropdown: function() {
		this.searchDropdown.removeClass("search-hidden");
		this.searchDropdown.store("visible", true);
		$("searchForm").focus()
	},
	hideSearchDropdown: function() {
		this.searchDropdown.addClass("search-hidden");
		this.searchDropdown.store("visible", false);
		$("searchForm").blur()
	}
};

window.addEvent("domready",
function() {
	HeaderManager.initialize();
	$$("#menu-button").addEvent("click")
});