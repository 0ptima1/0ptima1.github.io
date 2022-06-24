---
title: Projects
layout: landing
description: "Model Implementation from End to End<br> based on thorough understanding"
image: assets/images/dsl_original.jpg
nav-menu: true
---

<!-- Main -->
<div id="main">

<!-- Cover -->
<section id="one">
	<div class="inner">
		<header class="major">
			<h2>Deep Learning</h2>
		</header>
		<p>CNN based models such as Mask RCNN and FishNet.</p>
	</div>
</section>

<!-- projects -->
<section id="two" class="spotlights">
	<section>
		<span class="image">
			<img src="{% link assets/images/projects/mask_rcnn.png %}" alt="" data-position="center center" />
		</span>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Recommendation based on Instance Segmentation and Data Embedding</h3>
				</header>
				<p>This service recommends outfit based on what kind of clothes user has. In the first step, 
                    users upload their own clothes such as shirt or outwear in their own closet. 
                    Then, this model can recognize clothes in the image and find out the most similar items in the database. 
                    Finally, this service searches for the outfit which contains that similar items and offers 
                    a series of outfit and its link so that user can buy that outfit if they want.
                </p>
				<ul class="actions">
					<li><a href="https://github.com/yejin109/MaskRCNN-Recommendation" class="button small">source</a></li>
				</ul>
			</div>
		</div>
	</section>
    <section>
		<span class="image">
			<img src="{% link assets/images/projects/fishnet.jpg %}" alt="" data-position="top center" />
		</span>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Implementation of FishNet: A Versatile Backbone for Image, Region and Pixel Level Prediction</h3>
				</header>
				<p>
                    해당 프로젝트는 로컬에서 진행한 것으로 사용한 GPU는 1660S이기 때문에 원문에서 제안하는 모델을 경량화하여 구현한 것입니다.
                </p>
				<ul class="actions">
					<li><a href="https://github.com/yejin109/FishNet_Pytorch" class="button small">source</a></li>
				</ul>
			</div>
		</div>
	</section>	
	<section>
		<span class="image">
			<img src="{% link assets/images/projects/data_driven_social.png %}" alt="" data-position="top center" />
		</span>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Data-driven Social problem solution Competition</h3>
				</header>
				<p>
                    온라인 커뮤니티에서 사용되는 표현들의 특징을 소수의 라벨 정보를 이용하여 관계를 파악하고, 부적절한 표현을 탐지하는 모델로,
                    크롤링부터 토큰 임베딩 학습 그리고 최종 클러스터링까지 End-to-End로 구현한 프로젝트 입니다.
                </p>
				<ul class="actions">
					<li><a href="https://github.com/yejin109/Data-based-Social-Problem-Solution-Project" class="button small">source</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>

<section id="one">
	<div class="inner">
		<header class="major">
			<h2>Distributed Learning</h2>
		</header>
		<p>Learning Framework for the data-distributed system. Try to exploit the diversity of networks of several devices</p>
	</div>
</section>

<section id="two" class="spotlights">
	<section>
		<span class="image">
			<img src="{% link assets/images/projects/distributed_learning.jpg %}" alt="" data-position="center center" />
		</span>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Data Importance-Aware Scheduling for Exploiting Diversity of Distributed Data</h3>
				</header>
				<p>
                    In this study, we present a data importance (DI)-aware scheduling method for wireless communication 
                    systems in which the edge server has only a limited amount of information acquired by a subset of 
                    edge devices having their local datasets. We first characterize a DI metric, which quantifies the 
                    similarity between two distributions of the global dataset and the subset of local datasets, and 
                    then devise our scheduler along with the DI metric. Experimental results using the MNIST dataset 
                    demonstrate that the DI-aware scheduling is effective while providing potential gains over random selection.    
                </p>
				<ul class="actions">
					<li><a href="https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11047530" class="button small">paper</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>

</div>
