---
layout: post
title: whitePad
description: test here
image: 
---

<h1>Post</h1>
{%for post in site.posts%}
<p>{{post.title}}</p>
{% endfor%}

<h1> Page</h1>
{%for page in site.pages%}
<p>{{page.title}}</p>
{% endfor%}

