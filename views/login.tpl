<form method="post" action="/login">
<table>
<tr><td>Username:</td><td><input type="text" name="username" size="20"></td></tr>
<tr><td>Password:</td><td><input type="password" name="password" size="20"></td></tr>
<tr><td><input type="submit" value="Log in"></td><td>&nbsp;</td></tr>
</table>
</form>
%rebase _layout title='Login', username=username
