# A movie website
Running instructions: 
There is a submodule that I have tried to include here that has the starter code from udacity, to clone that too you will need to run the --recurse-submodules arguement to the clone command
you will just have to run the commands below to get the repo as well as its dependency, the udacity starter code. 

```
git clone --recurse-submodules https://github.com/pranav97/movie_website.git
cd movie_website
python entertainment_centre.py
```
If python isn't installed, you need to run this command to get that installed
and set up
```
sudo apt install python
```
On windows,[click me](https://www.python.org/downloads/ "Python downloads") to download Python.
(You can download either 2.x or 3.x)

## File Structure

The file `movie_posters` has all the raw images that go into the webpage while
it is being generated by fresh_tomatos.py.

`media.py` has the classes called movies. This class has an documentation of
its own inside it.

`entertainment_centre.py` creates the instances of the movies that are my
favorite and then calls fresh_tomatos from the udacity starter code to
generate the website. And then opens the generated website in the default
webbrowser.

## Ownership
I only wrote the code that is contained in this repository, I did not write the html code that is making the webpage. All that starter code is a submodule of this and was provided by Udacity.com
