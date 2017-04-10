function checkadd() {
	var ipt
	var textboxs = new Array();
	var inputs = row_add.getElementsByTagName("input");
	var check = 0
	for (var i=0; i<inputs.length; i++) { 
		ipt = inputs[i]; 
		if (ipt.type == "text") { 
			textboxs[textboxs.length] = ipt;
		} 
	}
	for (var i=0; i<textboxs.length; i++){
		var txt = textboxs[i];
		if (txt && txt.value != "")
			check = 1
	}

	if (check == 1){
		return true;
	}
	alert("请输入至少一个字段");
	return false;
}