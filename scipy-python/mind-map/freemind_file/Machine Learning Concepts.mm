<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1518790672151" ID="ID_55479794" MODIFIED="1518790775648" TEXT="Machine Learning Concepts">
<node CREATED="1518790730358" ID="ID_443896267" MODIFIED="1518790732188" POSITION="left" TEXT="Motivation">
<node CREATED="1518790858194" ID="ID_157124941" MODIFIED="1518790859345" TEXT="Prediction">
<node CREATED="1518790870826" ID="ID_1075041530" MODIFIED="1518790871421" TEXT="When we are interested mainly in the predicted variable as a result of the inputs, but not on the each way of the inputs affect the prediction. In a real estate example, Prediction would answer the question of: Is my house over or under valued? Non-linear models are very good at these sort of predictions, but not great for inference because the models are much less interpretable."/>
</node>
<node CREATED="1518790962952" ID="ID_1237798225" MODIFIED="1518790965076" TEXT="Inference">
<node CREATED="1518790978543" ID="ID_949147363" MODIFIED="1518790980099" TEXT="When we are interested in the way each one of the inputs affect the prediction. In a real estate example, Inference would answer the question of: How much would my house cost if it had a view of the sea? Linear models are more suited for inference because the models themselves are easier to understand than their non-linear counterparts."/>
</node>
</node>
<node CREATED="1518790747852" ID="ID_1930340171" MODIFIED="1518790749226" POSITION="left" TEXT="Performance Analysis">
<node CREATED="1518791040630" ID="ID_116702796" MODIFIED="1518791041338" TEXT="Confusion Matrix"/>
<node CREATED="1518791208506" ID="ID_1334027350" MODIFIED="1518791209182" TEXT="Accuracy">
<node CREATED="1518791218082" ID="ID_1402583280" MODIFIED="1518791218710" TEXT="Fraction of correct predictions, not reliable as skewed when the data set is unbalanced (that is, when the number of samples in different classes vary greatly)"/>
</node>
<node CREATED="1518791275545" ID="ID_194753165" MODIFIED="1518791276237" TEXT="f1 score">
<node CREATED="1518791432261" ID="ID_867199694" MODIFIED="1518791432905" TEXT="Precision">
<node CREATED="1518791447829" ID="ID_1306618716" MODIFIED="1518791448369" TEXT="Out of all the examples the classifier labeled as positive, what fraction were correct?"/>
</node>
<node CREATED="1518791477127" ID="ID_317019373" MODIFIED="1518791477824" TEXT="Recall">
<node CREATED="1518791490255" ID="ID_1999126869" MODIFIED="1518791490696" TEXT="Out of all the positive examples there were, what fraction did the classifier pick up?"/>
</node>
<node CREATED="1518791521779" ID="ID_1808972984" MODIFIED="1518791523080" TEXT="Harmonic Mean of Precision and Recall: (2 * p * r / (p + r))"/>
</node>
<node CREATED="1518791542739" ID="ID_43222862" MODIFIED="1518791543471" TEXT="ROC Curve - Receiver Operating Characteristics">
<node CREATED="1518791557315" ID="ID_1141436197" MODIFIED="1518791558007" TEXT="True Positive Rate (Recall / Sensitivity) vs False Positive Rate (1-Specificity)"/>
</node>
<node CREATED="1518791615338" ID="ID_1165990052" MODIFIED="1518791616277" TEXT="Bias-Variance Tradeoff">
<node CREATED="1518791626033" ID="ID_1845384062" MODIFIED="1518791626557" TEXT="Bias refers to the amount of error that is introduced by approximating a real-life problem, which may be extremely complicated, by a simple model. If Bias is high, and/or if the algorithm performs poorly even on your training data, try adding more features, or a more flexible model."/>
<node CREATED="1518791712519" ID="ID_1402993492" MODIFIED="1518791713459" TEXT="Variance is the amount our model&#x2019;s prediction would change when using a different training data set. High: Remove features, or obtain more data."/>
</node>
<node CREATED="1518791746343" ID="ID_633943924" MODIFIED="1518791746787" TEXT="Goodness of Fit = R^2">
<node CREATED="1518791759031" ID="ID_1122072905" MODIFIED="1518791759682" TEXT="1.0 - sum_of_squared_errors / total_sum_of_squares(y)"/>
</node>
<node CREATED="1518791773030" ID="ID_1536324524" MODIFIED="1518791773570" TEXT="Mean Squared Error (MSE)">
<node CREATED="1518791784846" ID="ID_560120223" MODIFIED="1518791785330" TEXT="The mean squared error (MSE) or mean squared deviation (MSD) of an estimator (of a procedure for estimating an unobserved quantity) measures the average of the squares of the errors or deviations&#x2014;that is, the difference between the estimator and what is estimated."/>
</node>
<node CREATED="1518791827669" ID="ID_205027124" MODIFIED="1518791828137" TEXT="Error Rate">
<node CREATED="1518791835989" ID="ID_548289889" MODIFIED="1518791879256" TEXT="The proportion of mistakes made if we apply out estimate model function the training observations in a classification setting."/>
</node>
</node>
<node CREATED="1518790760628" ID="ID_49793772" MODIFIED="1518790761722" POSITION="left" TEXT="Tuning">
<node CREATED="1518791992601" ID="ID_1772718399" MODIFIED="1518791993094" TEXT="Cross-validation">
<node CREATED="1518792007057" ID="ID_23700557" MODIFIED="1518792007661" TEXT="One round of cross-validation involves partitioning a sample of data into complementary subsets, performing the analysis on one subset (called the training set), and validating the analysis on the other subset (called the validation set or testing set). To reduce variability, multiple rounds of cross-validation are performed using different partitions, and the validation results are averaged over the rounds."/>
<node CREATED="1518792045784" ID="ID_1444852689" MODIFIED="1518792046516" TEXT="Methods">
<node CREATED="1518792054496" ID="ID_1178055084" MODIFIED="1518792055125" TEXT="Leave-p-out cross-validation"/>
<node CREATED="1518792130630" ID="ID_308724258" MODIFIED="1518792131098" TEXT="Leave-one-out cross-validation"/>
<node CREATED="1518792138350" ID="ID_18468502" MODIFIED="1518792138842" TEXT="k-fold cross-validation"/>
<node CREATED="1518792145142" ID="ID_108961671" MODIFIED="1518792145754" TEXT="Holdout method"/>
<node CREATED="1518792283227" ID="ID_1276174" MODIFIED="1518792283911" TEXT="Repeated random sub-sampling validation"/>
</node>
</node>
<node CREATED="1518792382961" ID="ID_744736260" MODIFIED="1518792383629" TEXT="Hyperparameters">
<node CREATED="1518792392913" ID="ID_1748899028" MODIFIED="1518792394514" TEXT="Grid Search">
<node CREATED="1518792405753" ID="ID_494129279" MODIFIED="1518792410861" TEXT="The traditional way of performing hyperparameter optimization has been grid search, or a parameter sweep, which is simply an exhaustive searching through a manually specified subset of the hyperparameter space of a learning algorithm. A grid search algorithm must be guided by some performance metric, typically measured by cross-validation on the training set or evaluation on a held-out validation set."/>
</node>
<node CREATED="1518793078699" ID="ID_644430934" MODIFIED="1518793079447" TEXT="Random Search">
<node CREATED="1518793089834" ID="ID_1653467925" MODIFIED="1518793092738" TEXT="Since grid searching is an exhaustive and therefore potentially expensive method, several alternatives have been proposed. In particular, a randomized search that simply samples parameter settings a fixed number of times has been found to be more effective in high- dimensional spaces than exhaustive search."/>
</node>
<node CREATED="1518793119370" ID="ID_1775693588" MODIFIED="1518793120077" TEXT="Gradient-based optimization">
<node CREATED="1518793129169" ID="ID_1580569790" MODIFIED="1518793129885" TEXT="For specific learning algorithms, it is possible to compute the gradient with respect to hyperparameters and then optimize the hyperparameters using gradient descent. The first usage of these techniques was focused on neural networks. Since then, these methods have been extended to other models such as support vector machines or logistic regression."/>
</node>
</node>
<node CREATED="1518793180800" ID="ID_1348169748" MODIFIED="1518793182044" TEXT="Early Stopping (Regularization)">
<node CREATED="1518793196208" ID="ID_757819888" MODIFIED="1518793196860" TEXT="Early stopping rules provide guidance as to how many iterations can be run before the learner begins to over-fit, and stop the algorithm then."/>
</node>
<node CREATED="1518793218847" ID="ID_525297970" MODIFIED="1518793219611" TEXT="Overfitting">
<node CREATED="1518793228863" ID="ID_170380009" MODIFIED="1518793229483" TEXT="When a given method yields a small training MSE (or cost), but a large test MSE (or cost), we are said to be overfitting the data. This happens because our statistical learning procedure is trying too hard to find pattens in the data, that might be due to random chance, rather than a property of our function. In other words, the algorithms may be learning the training data too well. If model overfits, try removing some features, decreasing degrees of freedom, or adding more data."/>
</node>
<node CREATED="1518793281238" ID="ID_545450364" MODIFIED="1518793281730" TEXT="Underfitting">
<node CREATED="1518793289574" ID="ID_592314141" MODIFIED="1518793290002" TEXT="Opposite of Overfitting. Underfitting occurs when a statistical model or machine learning algorithm cannot capture the underlying trend of the data. It occurs when the model or algorithm does not fit the data enough. Underfitting occurs if the model or algorithm shows low variance but high bias (to contrast the opposite, overfitting from high variance and low bias). It is often a result of an excessively simple model."/>
</node>
<node CREATED="1518793296686" ID="ID_1984237695" MODIFIED="1518793344619" TEXT="Bootstrap">
<node CREATED="1518793304262" ID="ID_647879449" MODIFIED="1518793304817" TEXT="Test that applies Random Sampling with Replacement of the available data, and assigns measures of accuracy (bias, variance, etc.) to sample estimates."/>
</node>
<node CREATED="1518793792203" ID="ID_13764353" MODIFIED="1518793792967" TEXT="Bagging">
<node CREATED="1518793800363" ID="ID_1683962619" MODIFIED="1518793800871" TEXT="An approach to ensemble learning that is based on bootstrapping. Shortly, given a training set, we produce multiple different training sets (called bootstrap samples), by sampling with replacement from the original dataset. Then, for each bootstrap sample, we build a model. The results in an ensemble of models, where each model votes with the equal weight. Typically, the goal of this procedure is to reduce the variance of the model of interest (e.g. decision trees)."/>
</node>
</node>
<node CREATED="1518790776500" ID="ID_1410727717" MODIFIED="1518790777183" POSITION="right" TEXT="Types">
<node CREATED="1518856617278" ID="ID_1389611331" MODIFIED="1518856619572" TEXT="Regression">
<node CREATED="1518856631678" ID="ID_960916213" MODIFIED="1518856633011" TEXT="A supervised problem, the outputs are continuous rather than discrete."/>
</node>
<node CREATED="1518856649237" ID="ID_1160174202" MODIFIED="1518856651119" TEXT="Classification">
<node CREATED="1518856661821" ID="ID_848337630" MODIFIED="1518856663083" TEXT="Inputs are divided into two or more classes, and the learner must produce a model that assigns unseen inputs to one or more (multi-label classification) of these classes. This is typically tackled in a supervised way."/>
</node>
<node CREATED="1518856736420" ID="ID_1109111325" MODIFIED="1518856737055" TEXT="Clustering">
<node CREATED="1518856748763" ID="ID_312577561" MODIFIED="1518856749399" TEXT="A set of inputs is to be divided into groups. Unlike in classification, the groups are not known beforehand, making this typically an unsupervised task."/>
</node>
<node CREATED="1518856781458" ID="ID_1205011666" MODIFIED="1518856782086" TEXT="Density Estimation">
<node CREATED="1518856791338" ID="ID_1839097683" MODIFIED="1518856791838" TEXT="Finds the distribution of inputs in some space."/>
</node>
<node CREATED="1518858993660" ID="ID_709136005" MODIFIED="1518858994168" TEXT="Dimensionality Reduction">
<node CREATED="1518859008299" ID="ID_1357989239" MODIFIED="1518859008839" TEXT="Simplifies inputs by mapping them into a lower-dimensional space."/>
</node>
</node>
<node CREATED="1518790783291" ID="ID_1921638841" MODIFIED="1518790784135" POSITION="right" TEXT="Kind">
<node CREATED="1518859024275" ID="ID_1897777751" MODIFIED="1518859024751" TEXT="Parametric">
<node CREATED="1518859038171" ID="ID_611451363" MODIFIED="1518859038703" TEXT="Step 1: Making an assumption about the functional form or shape of our function (f), i.e.: f is linear, thus we will select a linear model."/>
<node CREATED="1518859065746" ID="ID_1490040713" MODIFIED="1518859066134" TEXT="Step 2: Selecting a procedure to fit or train our model. This means estimating the Beta parameters in the linear function. A common approach is the (ordinary) least squares, amongst others."/>
</node>
<node CREATED="1518859112345" ID="ID_649513312" MODIFIED="1518859112773" TEXT="Non-Parametric">
<node CREATED="1518859122017" ID="ID_935062375" MODIFIED="1518859122485" TEXT="When we do not make assumptions about the form of our function (f). However, since these methods do not reduce the problem of estimating f to a small number of parameters, a large number of observations is required in order to obtain an accurate estimate for f. An example would be the thin-plate spline model."/>
</node>
</node>
<node CREATED="1518790789147" ID="ID_1822173034" MODIFIED="1518790789527" POSITION="right" TEXT="Categories">
<node CREATED="1518859403947" ID="ID_413793285" MODIFIED="1518859404503" TEXT="Supervised">
<node CREATED="1518859419419" ID="ID_56007297" MODIFIED="1518859419855" TEXT="The computer is presented with example inputs and their desired outputs, given by a &quot;teacher&quot;, and the goal is to learn a general rule that maps inputs to outputs."/>
</node>
<node CREATED="1518859441474" ID="ID_67199485" MODIFIED="1518859441846" TEXT="Unsupervised">
<node CREATED="1518859452218" ID="ID_499085272" MODIFIED="1518859452646" TEXT="No labels are given to the learning algorithm, leaving it on its own to find structure in its input. Unsupervised learning can be a goal in itself (discovering hidden patterns in data) or a means towards an end (feature learning)."/>
</node>
<node CREATED="1518859511865" ID="ID_80504616" MODIFIED="1518859512421" TEXT="Reinforcement Learning">
<node CREATED="1518859525465" ID="ID_829180626" MODIFIED="1518859525868" TEXT="A computer program interacts with a dynamic environment in which it must perform a certain goal (such as driving a vehicle or playing a game against an opponent). The program is provided feedback in terms of rewards and punishments as it navigates its problem space."/>
</node>
</node>
<node CREATED="1518790796243" ID="ID_816505691" MODIFIED="1518790796767" POSITION="right" TEXT="Approaches">
<node CREATED="1518859609631" ID="ID_667320620" MODIFIED="1518859612122" TEXT="Decision tree learning"/>
<node CREATED="1518859621927" ID="ID_1367268615" MODIFIED="1518859622315" TEXT="Association rule learning"/>
<node CREATED="1518859706717" ID="ID_610836576" MODIFIED="1518859707225" TEXT="Artificial neural networks"/>
<node CREATED="1518859718013" ID="ID_47825824" MODIFIED="1518859718504" TEXT="Deep learning"/>
<node CREATED="1518859728028" ID="ID_1673310832" MODIFIED="1518859729592" TEXT="Inductive logic programming"/>
<node CREATED="1518859929152" ID="ID_1232838846" MODIFIED="1518859929652" TEXT="Support vector machines"/>
<node CREATED="1518859935776" ID="ID_1639356533" MODIFIED="1518859936308" TEXT="Clustering"/>
<node CREATED="1518859945712" ID="ID_411083318" MODIFIED="1518859946212" TEXT="Bayesian networks"/>
<node CREATED="1518859953416" ID="ID_1828466308" MODIFIED="1518859954196" TEXT="Reinforcement learning"/>
<node CREATED="1518860008894" ID="ID_1746660981" MODIFIED="1518860009522" TEXT="Representation learning"/>
<node CREATED="1518860560259" ID="ID_1268364722" MODIFIED="1518860560967" TEXT="Similarity and metric learning"/>
<node CREATED="1518860641281" ID="ID_1647080743" MODIFIED="1518860641813" TEXT="Sparse dictionary learning"/>
<node CREATED="1518861486576" ID="ID_1253288402" MODIFIED="1518861487060" TEXT="Genetic algorithms"/>
<node CREATED="1518861507079" ID="ID_484624046" MODIFIED="1518861507539" TEXT="Rule-based machine learning"/>
<node CREATED="1518861601941" ID="ID_1678692669" MODIFIED="1518861603196" TEXT="Learning classifier systems"/>
</node>
<node CREATED="1518790804683" ID="ID_1052775256" MODIFIED="1518790805254" POSITION="right" TEXT="Taxonomy">
<node CREATED="1518861685435" ID="ID_1944743698" MODIFIED="1518861685887" TEXT="Generative Methods">
<node CREATED="1518861713707" ID="ID_1318287240" MODIFIED="1518861714183" TEXT="Model class-conditional pdfs and prior probabilities. &#x201c;Generative&#x201d; since sampling can generate synthetic data points."/>
<node CREATED="1518861824457" ID="ID_1751018740" MODIFIED="1518861824924" TEXT="Popular models">
<node CREATED="1518861833896" ID="ID_857621002" MODIFIED="1518861834300" TEXT="Gaussians, Na&#xef;ve Bayes, Mixtures of multinomials"/>
<node CREATED="1518861854944" ID="ID_1340236120" MODIFIED="1518861855332" TEXT="Mixtures of Gaussians, Mixtures of experts, Hidden Markov Models (HMM)"/>
<node CREATED="1518861868520" ID="ID_1199799776" MODIFIED="1518861868979" TEXT="Sigmoidal belief networks, Bayesian networks, Markov random fields"/>
</node>
</node>
<node CREATED="1518861882759" ID="ID_399801788" MODIFIED="1518861883147" TEXT="Discriminative Methods">
<node CREATED="1518861892095" ID="ID_37579891" MODIFIED="1518861892563" TEXT="Directly estimate posterior probabilities. No attempt to model underlying probability distributions. Focus computational resources on given task&#x2013; better performance"/>
<node CREATED="1518861900807" ID="ID_957196007" MODIFIED="1518861901219" TEXT="Popular Models">
<node CREATED="1518861911967" ID="ID_1592336163" MODIFIED="1518861912427" TEXT="Logistic regression, SVMs"/>
<node CREATED="1518861926854" ID="ID_461199788" MODIFIED="1518861927370" TEXT="Traditional neural networks, Nearest neighbor"/>
<node CREATED="1518861940238" ID="ID_903968508" MODIFIED="1518861960546" TEXT="Conditional Random Fields (CRF)"/>
</node>
</node>
</node>
<node CREATED="1518790811611" ID="ID_1643025898" MODIFIED="1518790812073" POSITION="right" TEXT="Selection Criteria">
<node CREATED="1518861978645" ID="ID_800560967" MODIFIED="1518861979113" TEXT="Prediction Accuracy vs Model Interpretability">
<node CREATED="1518862001637" ID="ID_1200419215" MODIFIED="1518862002073" TEXT="There is an inherent tradeoff between Prediction Accuracy and Model Interpretability, that is to say that as the model get more flexible in the way the function (f) is selected, they get obscured, and are hard to interpret. Flexible methods are better for inference, and inflexible methods are preferable for prediction."/>
</node>
</node>
<node CREATED="1518790817707" ID="ID_459907225" MODIFIED="1518790818102" POSITION="right" TEXT="Libraries">
<node CREATED="1518862049916" ID="ID_1884065531" MODIFIED="1518862050312" TEXT="Python">
<node CREATED="1518862059572" ID="ID_1630875752" MODIFIED="1518862059959" TEXT="Numpy">
<node CREATED="1518862071163" ID="ID_1068717905" MODIFIED="1518862071615" TEXT="Adds support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays"/>
</node>
<node CREATED="1518862117554" ID="ID_1633036213" MODIFIED="1518862118238" TEXT="Pandas">
<node CREATED="1518862132082" ID="ID_470968833" MODIFIED="1518862132758" TEXT="Offers data structures and operations for manipulating numerical tables and time series"/>
</node>
<node CREATED="1518862143970" ID="ID_1555612882" MODIFIED="1518862144358" TEXT="Scikit-Learn">
<node CREATED="1518862152178" ID="ID_1158117154" MODIFIED="1518862152621" TEXT="It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k- means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy."/>
</node>
<node CREATED="1518862184849" ID="ID_1231072908" MODIFIED="1518862185229" TEXT="Tensorflow">
<node CREATED="1518862200537" ID="ID_981659367" MODIFIED="1518862200892" TEXT="Components">
<node CREATED="1518862215352" ID="ID_725665553" MODIFIED="1518862215900" TEXT="Does lazy evaluation. Need to build the graph, and then run it in a session."/>
</node>
</node>
<node CREATED="1518862239344" ID="ID_826997974" MODIFIED="1518862241118" TEXT="MXNet">
<node CREATED="1518862247520" ID="ID_699783841" MODIFIED="1518862247923" TEXT="Is an modern open-source deep learning framework used to train, and deploy deep neural networks. MXNet library is portable and can scale to multiple GPUs and multiple machines. MXNet is supported by major Public Cloud providers including AWS and Azure. Amazon has chosen MXNet as its deep learning framework of choice at AWS."/>
</node>
<node CREATED="1518862282503" ID="ID_1619690478" MODIFIED="1518862284063" TEXT="Keras">
<node CREATED="1518862289287" ID="ID_258831980" MODIFIED="1518862289619" TEXT="Is an open source neural network library written in Python. It is capable of running on top of MXNet, Deeplearning4j, Tensorflow, CNTK or Theano. Designed to enable fast experimentation with deep neural networks, it focuses on being minimal, modular and extensible."/>
</node>
<node CREATED="1518862324398" ID="ID_1255585368" MODIFIED="1518862324674" TEXT="Torch">
<node CREATED="1518862335191" ID="ID_1518561586" MODIFIED="1518862335506" TEXT="Torch is an open source machine learning library, a scientific computing framework, and a script language based on the Lua programming language. It provides a wide range of algorithms for deep machine learning, and uses the scripting language LuaJIT, and an underlying C implementation."/>
</node>
<node CREATED="1518862369205" ID="ID_1862022684" MODIFIED="1518862369577" TEXT="Microsoft Cognitive Toolkit">
<node CREATED="1518862386917" ID="ID_1412834294" MODIFIED="1518862387249" TEXT="Previously known as CNTK and sometimes styled as The Microsoft Cognitive Toolkit, is a deep learning framework developed by Microsoft Research. Microsoft Cognitive Toolkit describes neural networks as a series of computational steps via a directed graph."/>
</node>
</node>
</node>
</node>
</map>
