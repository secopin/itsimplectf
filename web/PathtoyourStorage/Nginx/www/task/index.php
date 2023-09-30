<!doctype html>
<html class="no-js" lang="">

<head>
<meta charset="utf-8">
<meta name="description" content="">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Enroll</title>
<link rel="stylesheet" href="css/bootstrap.min.css">
<link rel="stylesheet" href="css/flexslider.css">
<link rel="stylesheet" href="css/jquery.fancybox.css">
<link rel="stylesheet" href="css/main.css">
<link rel="stylesheet" href="css/responsive.css">
<link rel="stylesheet" href="css/font-icon.css">
<link rel="stylesheet" href="css/animate.min.css"> 
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css"> 
</head>

<body>
<section class="banner" role="banner">
  <header id="header">
    <div class="header-content clearfix"> <a class="logo" href="index.html">Enroll</a>
      <nav class="navigation" role="navigation">
        <ul class="primary-nav">
		 <li><a href="/#banner">Home</a></li>
          <li><a href="/?s=services">Services</a></li>
          <li><a href="/?s=about">About</a></li> 
          <li><a href="/?s=gallery">Gallery</a></li>
          <li><a href="/?s=teams">Our Team</a></li>
          <li><a href="/?s=contact">Contact</a></li>
        </ul>
      </nav>
      <a href="#" class="nav-toggle">Menu<span></span></a> </div>
  </header>
    <div class="banner" id="banner"> 
	<div class="slider-banner">
            <div data-lazy-background="images/slides/1.jpg"> 
                <h3 data-pos="['68%', '-40%', '58%', '42%']" data-duration="700" data-effect="move">
                    Success
                </h3> <br>
                <p data-pos="['75%', '110%', '75%', '36%']" data-duration="700" data-effect="move">
                    Lorem ipsum dolor sitamet consectetur adipiscing
                </p> 
            </div>
            <div data-lazy-background="images/slides/2.jpg"> 
                <h3 data-pos="['75%', '-40%', '58%', '42%']" data-duration="700" data-effect="move">
                    Ultimate
                </h3> <br>
                <p data-pos="['75%', '110%', '75%', '36%']" data-duration="700" data-effect="move">
                    Lorem ipsum dolor sitamet consectetur adipiscing 
                </p>
            </div>
             
        </div>
    </div> 
</section>
<section id="intro" class="section intro">
  <div class="container">
    <div class="col-md-8 col-md-offset-2 text-center">
      <h3>Looking to grow your business?</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eu libero scelerisque ligula sagittis faucibus eget quis lacus.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </div>
  </div>
</section>
<?php
		$section = $_GET['s'];
		if(isset($section))
		{   
            $filteredSection = str_replace("../", "", $section);
			include("section/$filteredSection");
		}
?>
<section id="pricing5" data-section="pricing-5" class="data-section">
    <div class="container">
          <div class="section-header">
                <h2 class="wow fadeInDown animated">Pricing</h2>
                <p class="wow fadeInDown animated">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eget risus vitae massa <br> semper aliquam quis mattis quam.</p>
            </div>
         <div class="row">
            <div class="col-md-3 col-md-offset-1">
                <div class="table">
                    <h3 class="editContent">Basic</h3>
                    <h2 class="editContent">$13</h2>
                    <p class="editContent">Per Month</p>
                    <ul class="table-content">
                        <li class="editContent"><i class="fa fa-hdd-o"></i> 10 GB Storage</li>
                        <li class="editContent"><i class="fa fa-pie-chart"></i> 500 GB Bandwidth</li>
                        <li class="editContent"><i class="fa fa-envelope-o"></i> Email Support</li>
                        <li class="editContent"><i class="fa fa-cogs"></i> 24x7 Support</li>
                    </ul>

                    <div class="text-center text-uppercase">
                        <a href="#" class="btn btn-default-green-transparent-tiny editContent">Signup Now</a>
                    </div>
                </div>
            </div>

            <div class="col-md-4">
                <div class="table long-table">
                    <h3 class="editContent">Premium</h3>
                    <h2 class="editContent">$23</h2>
                    <p class="editContent">Per Month</p>
                    <ul class="table-content">
                        <li class="editContent"><i class="fa fa-hdd-o"></i> 10 GB Storage</li>
                        <li class="editContent"><i class="fa fa-pie-chart"></i> 500 GB Bandwidth</li>
                        <li class="editContent"><i class="fa fa-envelope-o"></i> Email Support</li>
                        <li class="editContent"><i class="fa fa-cogs"></i> 24x7 Support</li>
                    </ul>

                    <div class="text-center text-uppercase">
                        <a href="#" class="btn btn-default-blue-tiny editContent">Signup Now</a>
                    </div>
                </div>

            </div>

            <div class="col-md-3">
                <div class="table">
                    <h3 class="editContent">Developer</h3>
                    <h2 class="editContent">$33</h2>
                    <p class="editContent">Per Month</p>
                    <ul class="table-content">
                        <li class="editContent"><i class="fa fa-hdd-o"></i> 10 GB Storage</li>
                        <li class="editContent"><i class="fa fa-pie-chart"></i> 500 GB Bandwidth</li>
                        <li class="editContent"><i class="fa fa-envelope-o"></i> Email Support</li>
                        <li class="editContent"><i class="fa fa-cogs"></i> 24x7 Support</li>
                    </ul>

                    <div class="text-center text-uppercase">
                        <a href="#" class="btn btn-default-green-transparent-tiny editContent">Signup Now</a>
                    </div>
                </div>

            </div>
         </div>
    </div>
</section>

<footer class="footer">
<div class="container-fluid">
<div id="map-row" class="row">
    <div class="col-sm-8">    
    	<iframe width="100%" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src=""></iframe> 
       
    </div>
	 <div class="col-sm-4">
			<h2>Contact us</h2>
    		<address>
    			<strong>Company name</strong><br>
    			1234 Street Dr.<br>
    			Vancouver, BC<br>
    			Canada<br>
    			V6G 1G9<br>
    			<abbr title="Phone">Tel:</abbr> (604) 555-4321
    		</address>
			  © 2023 Company Name. Template by <a target="_blank" href="http://webthemez.com/interior-design/" title="Bootstrap Themes and HTML Templates">WebThemez.com</a>.<br/>
			  Find more <a target="_blank" href="http://webthemez.com/free-bootstrap-templates" title="Bootstrap Templates">Bootstrap Templates</a>
	 </div>
	 </div>
</div>
</footer>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script> 
<script src="js/bootstrap.min.js"></script> 
<script src="js/jquery.flexslider-min.js"></script> 
<script src="js/jquery.fancybox.pack.js"></script>  
<script src="js/modernizr.js"></script> 
<script src="js/main.js"></script> 
<script type="text/javascript" src="js/jquery.contact.js"></script> 
<script type="text/javascript" src="js/jquery.devrama.slider.min-0.9.4.js"></script>
<script type="text/javascript">
		$(document).ready(function(){
			$('.slider-banner').DrSlider({
				'transition': 'fade',
				showNavigation: false,
				progressColor: "#9e015e"
			});
		});
	</script> 
</body>
</html>
