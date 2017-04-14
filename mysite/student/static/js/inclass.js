function selectcourse()//下拉栏选择课程
		{
			   //需要实现控制可以加if() while()实现
			var t = document.getElementById("selectcourse");   
			var selectValue=t.options[t.selectedIndex].value;//获取select的值
			  //alert(selectValue);
			
			<!--alert(event)-->
			
			
			var post_data ={
			"name":selectValue,
			};
			
			$.ajax({
			  type : "POST", //要插入数据，所以是POST协议 
			  url : "/teacher/classajax/", //注意结尾的斜线，否则会出现500错误
			  data : post_data, //JSON数据
			  // data:"name=" + event,
			  success: function(mydata){
				document.getElementById("a").innerHTML = mydata["coursemess"];
				Showtable(mydata)
				document.getElementById("thenext").innerHTML= 1;
				document.getElementById("m").innerHTML = mydata["segment"][1][1];
				document.getElementById("s").innerHTML = 0;
				m = mydata["segment"][1][1];
				s = 0;
			  },
			  // dataType : 'json', //在ie浏览器下我没有加dataTpye结果报错，所以建议加上
			  // contentType : 'application/json',
			});
			
		}
		
		function Showtable(mydata)//打印学生列表
		{
			var row0 = document.getElementById('mytable').rows[0];  //给第一行换背景  
				row0.className = 'title'; 
				var tableObj = document.getElementById('mytable');  
				var rowNums = tableObj.rows.length;

				var length = tableObj.rows.length
				for(var i = 1; i < length;i++)//切换课程时清除之前打印的表
				{
					document.getElementById('mytable').deleteRow(1);
				}
				
				for(var k = 0; k < mydata["stuname"].length;k++)
				{
					var tableObj = document.getElementById('mytable');  
				    var rowNums = tableObj.rows.length;
					var rowObj = tableObj.insertRow(rowNums);  //添加一行 
					
					var cellObj0 = rowObj.insertCell(0);  //添加第一个单元格及其信息  
				    cellObj0.innerHTML = mydata["stuname"][k];  
					  
				    var cellObj1 = rowObj.insertCell(1);  //添加第二个单元格及其信息  
				    cellObj1.className = 'center';  
				    cellObj1.innerHTML = mydata["stugroup"][k]; 
						
					var cellObj2 = rowObj.insertCell(2);  //添加第三个单元格及其信息  
				    cellObj2.className = 'center';  
				    cellObj2.innerHTML = mydata["stugrade"][k]; 

				}
		}
		
		function Fenzu()//点击分组按钮分组
		{		
			var t = document.getElementById("selectcourse");   
			var selectValue=t.options[t.selectedIndex].value;//获取select的值
			var post_data ={
			"name":selectValue,
			};
			
			$.ajax({
			  type : "POST", //要插入数据，所以是POST协议 
			  url : "/teacher/fenzu/", //注意结尾的斜线，否则会出现500错误
			  data : post_data, //JSON数据
			  success: function(mydata){
				  Showtable(mydata);
				  
				  
			  },
			});
		}
		
		function Randstu()//随机选择学生
		{		
			var t = document.getElementById("selectcourse");   
			var selectValue=t.options[t.selectedIndex].value;//获取select的值
			var post_data ={
			"name":selectValue,
			};
			
			$.ajax({
			  type : "POST", //要插入数据，所以是POST协议 
			  url : "/teacher/randstu/", //注意结尾的斜线，否则会出现500错误
			  data : post_data, //JSON数据
			  success: function(mydata){
				  alert(mydata["cstu"]);
			  },
			});
		}
		
		function Randgroup()//随机选择小组
		{		
			var t = document.getElementById("selectcourse");   
			var selectValue=t.options[t.selectedIndex].value;//获取select的值
			var post_data ={
			"name":selectValue,
			};
			
			$.ajax({
			  type : "POST", //要插入数据，所以是POST协议 
			  url : "/teacher/randgroup/", //注意结尾的斜线，否则会出现500错误
			  data : post_data, //JSON数据
			  success: function(mydata){
				  alert(mydata["czu"]);
				  
				  
			  },
			});
		}
		
		function Nextseg()
		{
			document.getElementById("thenext").innerHTML++;
		}
		
		
		
		function showName(){  
		var index = Math.floor(Math.random()*mydata.length);  
		var name = mydata[index];  
		document.getElementById("showView").innerHTML = name;  
		idd=setTimeout("showName()",50);  
		}  
		var state = true;  
		var idd; 
		function sssss(){ 

			if(state){  
				showName();  
				state = false;  
			}  
			else{  
				clearTimeout(idd);  
				state = true;  
			}  
				  
		} 



		
		//倒计时
			var m = 0;
			var s = 0;
			//var m= document.getElementById("m").innerText;

            var mytime=null;  
            //开始倒计时  
            function doSubmit(){
                run(); 
				document.getElementById("randzu").disabled= true;
				document.getElementById("selectcourse").disabled= true;
                document.getElementById("sid").disabled=true;  
                document.getElementById("tid").disabled=false;  
                document.getElementById("gid").disabled=true;  
                return false;  
            }  
              
            //执行倒计时  
            function run(){  
                //输出
                document.getElementById('m').innerHTML = m;
				document.getElementById('s').innerHTML = s;;  
                s--;  
                if(s<0){  
                    s=59;  
                    m--;  
                    if(m<0){  
                        alert('时间到！');  
                            return;  
                    }  
                }  
                mytime = setTimeout("run()",1000);  
            }  
              
            //暂停  
            function doPause(){  
                if(mytime!=null){  
                    clearTimeout(mytime);  
                    mytime=null;  
                }  
                document.getElementById("tid").disabled=true;  
                document.getElementById("gid").disabled=false;  
            }  
              
            //继续  
            function doGo(){  
                run();  
                document.getElementById("tid").disabled=false;  
                document.getElementById("gid").disabled=true;  
            }
			
			function Grade()//评分
			{
				   //需要实现控制可以加if() while()实现
				var t = document.getElementById("selectcourse");   
				var selectValue=t.options[t.selectedIndex].value;//获取select的值
				//alert(selectValue);

				var post_data ={
				"name":selectValue,
				};
				
				$.ajax({
				  type : "POST", //要插入数据，所以是POST协议 
				  url : "/teacher/gradeteacher/", //注意结尾的斜线，否则会出现500错误
				  data : post_data, //JSON数据
				  // data:"name=" + event,
				  success: function(mydata){
					document.getElementById("stumess").style.visibility="hidden";//隐藏
					document.getElementById("ping").disabled=true;
				  },
				});
				
			}