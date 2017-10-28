
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="assets/img/favicon.png">

    <title>AgriTech</title>

    <!-- Bootstrap core CSS -->
    <link href="assets/css/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="assets/css/main.css" rel="stylesheet">

    <!-- Fonts from Google Fonts -->
	<link href='http://fonts.googleapis.com/css?family=Lato:300,400,900' rel='stylesheet' type='text/css'>
    
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <!-- Fixed navbar -->
    <div class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#"><b>AgriTech</b></a>
        </div>
        <div class="navbar-collapse collapse">
        </div><!--/.nav-collapse -->
      </div>
    </div>

	<div id="headerwrap">
		<div class="container">
			<div class="row">
				<div class="col-lg-6">
					<h1>Great yield is just a click away!</h1>
					<p>Upload an image of your land</p>
					<form class="form-inline" role="form" action="cropdata.php" method="post" enctype="multipart/form-data">
					  <div class="form-group">
					    <input width="200px" type="file" name="fileToUpload" id="fileToUpload" placeholder="Upload soil image">
					  </div>
					  <input type="submit" name="submit" value="Analyze" class="btn btn-warning btn-lg">
					  <?php 
					  $command = escapeshellcmd('python trial.py'); 
					  $output = shell_exec($command);
					  echo $output;
					  ?>
					</form>					
				</div><!-- /col-lg-6 -->
				
			</div><!-- /row -->
		</div><!-- /container -->
	</div><!-- /headerwrap -->
	
	<div class="container">
		<div class="row mt centered">
			<div class="col-lg-6 col-lg-offset-3">
				<h1>Embrace agriculture in harmony<br/>with technology</h1>
				<h3>Empowering today's generation to know, harness and nurture their soil with the help of emerging technology.</h3>
			</div>
		</div><!-- /row -->
		
		<div class="row mt centered">
			<div class="col-lg-4">
				<img src="assets/img/step1.png" width="300" alt="">
				<h4>1- Know your soil</h4>
				<p>Upload an image of your soil to know its type, fertility and much more.</p>
			</div><!--/col-lg-4 -->

			<div class="col-lg-4">
				<img src="assets/img/step2.png" width="180" alt="">
				<h4>2- What to grow</h4>
				<p>We help you know which crops can help you maximise profit within any timeframe of choice.</p>

			</div><!--/col-lg-4 -->

			<div class="col-lg-4">
				<img src="assets/img/step3.png" width="180" alt="">
				<h4>3 - Share your success</h4>
				<p>Away from stereotypes, we help you to successfully take up agriculture with the help of fascinating technology.</p>

			</div><!--/col-lg-4 -->
		</div><!-- /row -->
	</div><!-- /container -->
	

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
  </body>
</html>
