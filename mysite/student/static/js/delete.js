function $(obj){
	return document.getElementById(obj); 
} 

function row(id){
	this.id = $(id);
}

row.prototype = { 
	del:function(obj){ 
		var i = obj.parentNode.parentNode.rowIndex;
		updateData_del(obj);
		this.id.deleteRow(i);
	} 
}

function updateData_del(obj){
	var url = "/main/?op=delete&no=" + obj.parentNode.parentNode.rowIndex + "&sid=" + Math.random();
	var ajax = new XMLHttpRequest();
	ajax.open("GET",url,false);
	ajax.send(null);
}

function delRow(obj){  
	var row1 = new row("main"); 
	row1.del(obj); 
} 