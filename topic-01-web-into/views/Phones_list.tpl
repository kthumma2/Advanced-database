<html>
<body>
<h2> List of Phones </h2>
<hr/>
<table>
% for item in Phones_list:
 <tr>
<td> {{str(item['desc'])}} </td>
<td> <a href="/edit/{{str(item['id'])}}">Edit</a> </td>
<td> <a href="/delete/{{str(item['id'])}}">Delete</a> </td>
 </tr>
% end
</table>
<hr/>
<a href="/add"> Add New Phone ..</a>
</body>
</html>