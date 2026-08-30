from django.shortcuts import render

# Create your views here.

posts =[
    {
    'author': 'Jane Doe',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'August 27, 2018'
},
{
    'author': 'John Smith',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'September 3, 2018'
},
{
    'author': 'Emily Clark',
    'title': 'Blog Post 3',
    'content': 'Third post content',
    'date_posted': 'September 15, 2018'
},
{
    'author': 'Michael Brown',
    'title': 'Blog Post 4',
    'content': 'Fourth post content',
    'date_posted': 'October 2, 2018'
},
{
    'author': 'Sarah Johnson',
    'title': 'Blog Post 5',
    'content': 'Fifth post content',
    'date_posted': 'October 20, 2018'
},
{
    'author': 'David Lee',
    'title': 'Blog Post 6',
    'content': 'Sixth post content',
    'date_posted': 'November 5, 2018'
},
{
    'author': 'Anna White',
    'title': 'Blog Post 7',
    'content': 'Seventh post content',
    'date_posted': 'November 22, 2018'
},
{
    'author': 'Chris Green',
    'title': 'Blog Post 8',
    'content': 'Eighth post content',
    'date_posted': 'December 10, 2018'
},
{
    'author': 'Laura Adams',
    'title': 'Blog Post 9',
    'content': 'Ninth post content',
    'date_posted': 'December 28, 2018'
},
{
    'author': 'James Wilson',
    'title': 'Blog Post 10',
    'content': 'Tenth post content',
    'date_posted': 'January 14, 2019'
},
{
    'author': 'Olivia Martin',
    'title': 'Blog Post 11',
    'content': 'Eleventh post content',
    'date_posted': 'January 30, 2019'
},
{
    'author': 'Daniel Harris',
    'title': 'Blog Post 12',
    'content': 'Twelfth post content',
    'date_posted': 'February 12, 2019'
},
{
    'author': 'Sophia Turner',
    'title': 'Blog Post 13',
    'content': 'Thirteenth post content',
    'date_posted': 'February 28, 2019'
},
{
    'author': 'Matthew Scott',
    'title': 'Blog Post 14',
    'content': 'Fourteenth post content',
    'date_posted': 'March 9, 2019'
},
{
    'author': 'Grace Baker',
    'title': 'Blog Post 15',
    'content': 'Fifteenth post content',
    'date_posted': 'March 25, 2019'
},
{
    'author': 'Ethan Young',
    'title': 'Blog Post 16',
    'content': 'Sixteenth post content',
    'date_posted': 'April 8, 2019'
},
{
    'author': 'Chloe King',
    'title': 'Blog Post 17',
    'content': 'Seventeenth post content',
    'date_posted': 'April 22, 2019'
},
{
    'author': 'Ryan Wright',
    'title': 'Blog Post 18',
    'content': 'Eighteenth post content',
    'date_posted': 'May 6, 2019'
},
{
    'author': 'Natalie Hill',
    'title': 'Blog Post 19',
    'content': 'Nineteenth post content',
    'date_posted': 'May 21, 2019'
},
{
    'author': 'Kevin Moore',
    'title': 'Blog Post 20',
    'content': 'Twentieth post content',
    'date_posted': 'June 4, 2019'
}
]


def home(request):
    context={
        'posts': posts
    }
    return render(request, 'Blog_App/home.html',context)

def about(request):
    return render(request, 'Blog_App/about.html', {'title','About'})