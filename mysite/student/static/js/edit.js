var inputItem;
var activeItem;
var raw;

function getRaw(obj) {
	raw = obj.innerText
}

function updateData_edit(obj){
	var url = "/edit/?pos=" + obj.id + "&key=" + obj.value + "&sid=" + Math.random();
	var ajax = new XMLHttpRequest();
	ajax.open("GET",url,false);
	ajax.send(null);
}

function changeToText(obj) {
	if (obj && inputItem) {
		if (inputItem.value != "" && inputItem.value != raw) {
			obj.innerText = inputItem.value;
			updateData_edit(inputItem);
		}
		else{
			obj.innerText = raw;
		}
		inputItem = "";
	}
}

function changeToEdit(obj) {
	inputItem.value = obj.innerText;
	obj.innerHTML = '';
	obj.appendChild(inputItem);
	inputItem.focus();
	activeItem = obj;
}

document.ondblclick = function() {
	if (event.srcElement.tagName.toLowerCase() == "td" && event.srcElement.id != "no_edit") {
		if (!inputItem) {
			inputItem = document.createElement("input");
			inputItem.type = "text";
			inputItem.id = event.srcElement.id;
			inputItem.style.width = "96px";
		}
		getRaw(event.srcElement);
		changeToText();
		changeToEdit(event.srcElement);
	} else {
		event.returnValue = false;
		return false;
	}
}

document.onclick = function() {
	if (event.srcElement.parentNode == activeItem || event.srcElement == activeItem) return;
	else changeToText(activeItem);
}