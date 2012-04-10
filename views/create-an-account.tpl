<form method="post" action="/create-an-account">
<table>
<tr><td>Desired username:</td><td><input type="text" name="username" size="20"></td></tr>
<tr><td>Password:</td><td><input type="password" name="password" size="20"></td></tr>
<tr><td>Email address:</td><td><input type="text" name="email" size="30"></td></tr>
<tr><td><input type="submit" value="Create account"></td><td>&nbsp;</td></tr>
</table>
</form>
%rebase _layout title='Create an account', username=username
