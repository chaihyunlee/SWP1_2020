html = b"""
<html>
    <body>
        <form method="get" action="">
            x : <input type="number" name="x" value="x">
            y : <input type="number" name="y" value="y">
            <input type="submit">
        </form>
        <p>
	x + y = %(sum)s</br>
        x * y = %(product)s</br>
        </p>
    </body>
</html>
"""
