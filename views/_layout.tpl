<!doctype html>
<html>
<head>
<title>{{title}}</title>
</head>

<body>
%if username:
<p><a href="/">Home</a> | <a href="/about">About</a> |
    Logged in as {{username}} | <a href="/logout">log out</a></p>
%else:
<p><a href="/">Home</a> | <a href="/about">About</a> |
    <a href="/login">log in</a> | <a href="/create-an-account">create an account</a></p>
%end

<h1>{{title}}</h1>
<hr/>

%include

<hr/>
<p>{footer}</p>
</body>
</html>
