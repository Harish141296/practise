from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here
posts = [
    {
        "id":1,
        "title":'Let\'s explore python',
        "content":"Python Is Interpreted, High-Level, General purpose programming language. Widely used in the fields of web development, data science and machine learning."

    },{
        "id":2,
        "title":'Javascript Frontend tool',
        "content":"Javascript Is Interpreted, High-level, General purpose programming language. Widely used in the field of web development."
    },{
        "id":3,
        "title":'Django the best web framework',
        "content":"Python Is Interpreted, High-Level, General purpose programming language. Widely used in the fields of web development, data science and machine learning."
    },
]
def home(request):
    html = '<html><body><table border = 2><tr><th>ID<th>Title<th>Content</tr>'
    for post in posts:
        html += f"""
        <tr>
        <td><a href='/post/home/{post['id']}'>{post['id']}</a></td>
        <td>{post['title']}</td>
        <td>{post['content']}</td>   
        </tr>         
        """
    html += "</table></body></html>"
    return HttpResponse(html)

def detailPost(request, id):
    status = False 
    html = '<html><body><table border = 2><tr><th>ID<th>Title<th>Content</tr>'
    for post in posts:
        if id == post['id']:
            status = True 
            html += f"""
                    <tr>
                    <td><a href='/post/home'>{post['id']}</a></td>
                    <td>{post['title']}</td>
                    <td>{post['content']}</td>   
                    </tr>         
                    """
    if not status:
        html += f"<td colspan=3> No post available for this id: {id}"
    html += "</table></body></html>"
    return HttpResponse(html)