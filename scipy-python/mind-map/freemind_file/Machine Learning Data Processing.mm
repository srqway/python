<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1518763611691" ID="ID_1936554145" MODIFIED="1518763903564" TEXT="Machine Learning Data Processing">
<node CREATED="1518763695405" ID="ID_1638002631" MODIFIED="1518763732948" POSITION="left" TEXT="Data Types">
<node CREATED="1518764277416" ID="ID_629727900" MODIFIED="1518764783458" TEXT="Nominal">
<node CREATED="1518764825581" ID="ID_1809318447" MODIFIED="1518764880432" TEXT="Counts / Distributiion"/>
</node>
<node CREATED="1518764485164" ID="ID_393360548" MODIFIED="1518764803545" TEXT="Ordinal">
<node CREATED="1518764890540" ID="ID_273149161" MODIFIED="1518764914771" TEXT="Counts / Distributiion"/>
<node CREATED="1518764956715" ID="ID_1115365947" MODIFIED="1518765008173" TEXT="Minimum, Maximum"/>
<node CREATED="1518765092480" ID="ID_963047246" MODIFIED="1518765095587" TEXT="Range"/>
<node CREATED="1518765124183" ID="ID_672295628" MODIFIED="1518765127795" TEXT="Percentiles"/>
</node>
<node CREATED="1518764562331" ID="ID_807581010" MODIFIED="1518764806786" TEXT="Interval">
<node CREATED="1518764903627" ID="ID_1219985023" MODIFIED="1518764924543" TEXT="Counts / Distributiion"/>
<node CREATED="1518765024833" ID="ID_164306084" MODIFIED="1518765025765" TEXT="Minimum, Maximum"/>
<node CREATED="1518765104511" ID="ID_467600914" MODIFIED="1518765105011" TEXT="Range"/>
<node CREATED="1518765289788" ID="ID_173441227" MODIFIED="1518765290600" TEXT="Percentiles"/>
<node CREATED="1518765371250" ID="ID_1185614092" MODIFIED="1518765372262" TEXT="Standard deviation, Variance"/>
</node>
<node CREATED="1518764594242" ID="ID_153825997" MODIFIED="1518764810073" TEXT="Ratio">
<node CREATED="1518764931315" ID="ID_1498873874" MODIFIED="1518764932618" TEXT="Counts / Distributiion"/>
<node CREATED="1518765027929" ID="ID_130945291" MODIFIED="1518765029423" TEXT="Minimum, Maximum"/>
<node CREATED="1518765107047" ID="ID_203794201" MODIFIED="1518765108334" TEXT="Range"/>
<node CREATED="1518765293012" ID="ID_853451286" MODIFIED="1518765293592" TEXT="Percentiles"/>
<node CREATED="1518765310171" ID="ID_1159114386" MODIFIED="1518765347503" TEXT="Standard deviation, Variance"/>
</node>
</node>
<node CREATED="1518763740435" ID="ID_1224493739" MODIFIED="1518763751658" POSITION="left" TEXT="Data Exploration">
<node CREATED="1518765451384" ID="ID_1966851462" MODIFIED="1518765454232" TEXT="Variable Identification">
<node CREATED="1518765467520" ID="ID_1825942382" MODIFIED="1518765469247" TEXT="Identify Predictor (Input) and Target (output) variables. Next, identify the data type and category of the variables."/>
</node>
<node CREATED="1518765502391" ID="ID_1171249476" MODIFIED="1518765503291" TEXT="Univariate Analysis">
<node CREATED="1518765518975" ID="ID_1510769101" MODIFIED="1518765605323" TEXT="Continuous Features">
<node CREATED="1518765595821" ID="ID_1607125743" MODIFIED="1518765686076" TEXT="Mean, Median, Mode, Min, Max, Range, Quartile, IQR, Variance, Standard Deviation, Skewness, Histogram, Box Plot"/>
</node>
<node CREATED="1518765603597" ID="ID_1631286828" MODIFIED="1518765714553" TEXT="Categorical Features">
<node CREATED="1518765727379" ID="ID_179356556" MODIFIED="1518765728538" TEXT="Frequency, Histogram"/>
</node>
<node CREATED="1518765748250" ID="ID_808770777" MODIFIED="1518765749142" TEXT="Bi-variate Analysis">
<node CREATED="1518765762586" ID="ID_154107313" MODIFIED="1518765763526" TEXT="Finds out the relationship between two variables."/>
<node CREATED="1518765808881" ID="ID_1541537114" MODIFIED="1518765809725" TEXT="Scatter Plot"/>
<node CREATED="1518765819169" ID="ID_1811977024" MODIFIED="1518765820469" TEXT="Correlation Plot - Heatmap"/>
<node CREATED="1518765862360" ID="ID_667791004" MODIFIED="1518765863404" TEXT="Two-way table">
<node CREATED="1518765883040" ID="ID_1207781106" MODIFIED="1518765884091" TEXT="We can start analyzing the relationship by creating a two-way table of count and count%."/>
</node>
<node CREATED="1518765980102" ID="ID_766525549" MODIFIED="1518765981170" TEXT="Stacked Column Chart"/>
<node CREATED="1518765990853" ID="ID_199593107" MODIFIED="1518766036057" TEXT="Chi-Square Test">
<node CREATED="1518766004741" ID="ID_429307995" MODIFIED="1518766005465" TEXT="This test is used to derive the statistical significance of relationship between the variables."/>
</node>
<node CREATED="1518766033453" ID="ID_1208615929" MODIFIED="1518766034465" TEXT="Z-Test/ T-Test"/>
<node CREATED="1518766043701" ID="ID_631006792" MODIFIED="1518766044656" TEXT="ANOVA"/>
</node>
</node>
</node>
<node CREATED="1518763764243" ID="ID_47187199" MODIFIED="1518763765650" POSITION="left" TEXT="Feature Cleaning">
<node CREATED="1518766076548" ID="ID_389881332" MODIFIED="1518766077119" TEXT="Missing values">
<node CREATED="1518766147882" ID="ID_1316022857" MODIFIED="1518766149853" TEXT="One may choose to either omit elements from a dataset that contain missing values or to impute a value"/>
</node>
<node CREATED="1518766158946" ID="ID_1669115103" MODIFIED="1518772561405" TEXT="Special values">
<node CREATED="1518766174114" ID="ID_851322193" MODIFIED="1518766175456" TEXT="Numeric variables are endowed with several formalized special values including &#xb1;Inf, NA and NaN. Calculations involving special values often result in special values, and need to be handled/cleaned"/>
</node>
<node CREATED="1518772562631" ID="ID_1895852075" MODIFIED="1518772564035" TEXT="Outliers">
<node CREATED="1518772577919" ID="ID_114653657" MODIFIED="1518772579099" TEXT="They should be detected, but not necessarily removed. Their inclusion in the analysis is a statistical decision."/>
</node>
<node CREATED="1518772597534" ID="ID_156028377" MODIFIED="1518772598602" TEXT="Obvious inconsistencies">
<node CREATED="1518772610486" ID="ID_285640613" MODIFIED="1518772611450" TEXT="A person&apos;s age cannot be negative, a man cannot be pregnant and an under-aged person cannot possess a drivers license."/>
</node>
</node>
<node CREATED="1518763778107" ID="ID_516222911" MODIFIED="1518763784015" POSITION="left" TEXT="Feature Imputation">
<node CREATED="1518773059372" ID="ID_1122602044" MODIFIED="1518773060886" TEXT="Hot-Deck">
<node CREATED="1518773074652" ID="ID_837655763" MODIFIED="1518773075782" TEXT="The technique then finds the first missing value and uses the cell value immediately prior to the data that are missing to impute the missing value."/>
</node>
<node CREATED="1518773691399" ID="ID_732165471" MODIFIED="1518773704811" TEXT="Cold-Deck">
<node CREATED="1518773715152" ID="ID_947916391" MODIFIED="1518773717523" TEXT="Selects donors from another dataset to complete missing data."/>
</node>
<node CREATED="1518773997737" ID="ID_767967601" MODIFIED="1518773999485" TEXT="Mean-substitution">
<node CREATED="1518774015697" ID="ID_691204446" MODIFIED="1518774016868" TEXT="Another imputation technique involves replacing any missing value with the mean of that variable for all other cases, which has the benefit of not changing the sample mean for that variable."/>
</node>
<node CREATED="1518774034056" ID="ID_67165506" MODIFIED="1518774048020" TEXT="Regression">
<node CREATED="1518774067616" ID="ID_1641926200" MODIFIED="1518774068955" TEXT="A regression model is estimated to predict observed values of a variable based on other variables, and that model is then used to impute values in cases where that variable is missing"/>
</node>
</node>
<node CREATED="1518763797402" ID="ID_694294343" MODIFIED="1518772657249" POSITION="left" TEXT="Feature Engineering">
<node CREATED="1518772666861" ID="ID_580601252" MODIFIED="1518772667512" TEXT="Decompose">
<node CREATED="1518772684948" ID="ID_1006646664" MODIFIED="1518772686628" TEXT="Converting 2014-09-20T20:45:40Z into categorical attributes like hour_of_the_day, part_of_day, etc."/>
</node>
<node CREATED="1518772717131" ID="ID_718858135" MODIFIED="1518772718071" TEXT="Discretization">
<node CREATED="1518772777794" ID="ID_1594308833" MODIFIED="1518772779371" TEXT="Continuous Features">
<node CREATED="1518772816306" ID="ID_1810291124" MODIFIED="1518772817469" TEXT="Typically data is discretized into partitions of K equal lengths/width (equal intervals) or K% of the total data (equal frequencies)."/>
</node>
<node CREATED="1518772831249" ID="ID_1181537549" MODIFIED="1518772832053" TEXT="Categorical Features">
<node CREATED="1518772853353" ID="ID_529378256" MODIFIED="1518772854885" TEXT="Values for categorical features may be combined, particularly when there&#x2019;s few samples for some categories."/>
</node>
</node>
<node CREATED="1518772884000" ID="ID_552947644" MODIFIED="1518772884876" TEXT="Reframe Numerical Quantities">
<node CREATED="1518772895824" ID="ID_1066292682" MODIFIED="1518772896604" TEXT="Changing from grams to kg, and losing detail might be both wanted and efficient for calculation"/>
</node>
<node CREATED="1518772916159" ID="ID_768890018" MODIFIED="1518772916899" TEXT="Crossing">
<node CREATED="1518772928783" ID="ID_343473901" MODIFIED="1518772929739" TEXT="Creating new features as a combination of existing features. Could be multiplying numerical features, or combining categorical variables. This is a great way to add domain expertise knowledge to the dataset."/>
</node>
</node>
<node CREATED="1518763821410" ID="ID_1136632782" MODIFIED="1518763825373" POSITION="right" TEXT="Feature Selection">
<node CREATED="1518774791977" ID="ID_1370840301" MODIFIED="1518774794589" TEXT="Correlation">
<node CREATED="1518774826496" ID="ID_301488962" MODIFIED="1518774828735" TEXT="Features should be uncorrelated with each other and highly correlated to the feature we&#x2019;re trying to predict.">
<node CREATED="1518774879431" ID="ID_940104911" MODIFIED="1518774882013" TEXT="Covariance">
<node CREATED="1518774908622" ID="ID_1072669634" MODIFIED="1518774910741" TEXT="A measure of how much two random variables change together. Math: dot(de_mean(x), de_mean(y)) / (n - 1)"/>
</node>
</node>
</node>
<node CREATED="1518775214920" ID="ID_1934724967" MODIFIED="1518775217396" TEXT="Dimensionality Reduction">
<node CREATED="1518774970277" ID="ID_108289761" MODIFIED="1518774971881" TEXT="Principal Component Analysis (PCA)">
<node CREATED="1518774990732" ID="ID_462892338" MODIFIED="1518774993387" TEXT="Principal component analysis (PCA) is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components. This transformation is defined in such a way that the first principal component has the largest possible variance (that is, accounts for as much of the variability in the data as possible), and each succeeding component in turn has the highest variance possible under the constraint that it is orthogonal to the preceding components.">
<node CREATED="1518775161193" ID="ID_1092586744" MODIFIED="1518775163183" TEXT="Plot the variance per feature and select the features with the largest variance."/>
</node>
</node>
<node CREATED="1518775241896" ID="ID_1151051041" MODIFIED="1518775255179" TEXT="Singular Value Decomposition (SVD)">
<node CREATED="1518775274239" ID="ID_1864437460" MODIFIED="1518775276933" TEXT="SVD is a factorization of a real or complex matrix. It is the generalization of the eigendecomposition of a positive semidefinite normal matrix (for example, a symmetric matrix with positive eigenvalues) to any m&#xd7;n matrix via an extension of the polar decomposition. It has many useful applications in signal processing and statistics."/>
</node>
</node>
<node CREATED="1518775631743" ID="ID_16557428" MODIFIED="1518775632588" TEXT="Importance">
<node CREATED="1518775644521" ID="ID_778919104" MODIFIED="1518775645203" TEXT="Filter Methods">
<node CREATED="1518775670446" ID="ID_1005541035" MODIFIED="1518775749633" TEXT="Filter type methods select features based only on general metrics like the correlation with the variable to predict. Filter methods suppress the least interesting variables. The other variables will be part of a classification or a regression model used to classify or to predict data. These methods are particularly effective in computation time and robust to overfitting.">
<node CREATED="1518775733213" ID="ID_435241017" MODIFIED="1518775733777" TEXT="Correlation"/>
<node CREATED="1518775751301" ID="ID_469578792" MODIFIED="1518775789272" TEXT="Linear Discriminant Analysis (LDA)"/>
<node CREATED="1518775972456" ID="ID_1498285044" MODIFIED="1518775975924" TEXT="ANOVA: Analysis of Variance"/>
<node CREATED="1518775983648" ID="ID_331938406" MODIFIED="1518775986092" TEXT="Chi-Square"/>
</node>
</node>
<node CREATED="1518776014665" ID="ID_1248276169" MODIFIED="1518776015323" TEXT="Wrapper Methods">
<node CREATED="1518776023623" ID="ID_1097509428" MODIFIED="1518776024307" TEXT="Wrapper methods evaluate subsets of variables which allows, unlike filter approaches, to detect the possible interactions between variables. The two main disadvantages of these methods are : The increasing overfitting risk when the number of observations is insufficient. AND. The significant computation time when the number of variables is large.">
<node CREATED="1518776108613" ID="ID_938221886" MODIFIED="1518776109345" TEXT="Forward Selection"/>
<node CREATED="1518776239619" ID="ID_818643066" MODIFIED="1518776245783" TEXT="Backward Elimination"/>
<node CREATED="1518776261923" ID="ID_177671521" MODIFIED="1518776262510" TEXT="Recursive Feature Ellimination"/>
<node CREATED="1518776273458" ID="ID_532277338" MODIFIED="1518776274230" TEXT="Genetic Algorithms"/>
</node>
</node>
<node CREATED="1518776345017" ID="ID_1942292940" MODIFIED="1518776345540" TEXT="Embedded Methods">
<node CREATED="1518776355432" ID="ID_1491820762" MODIFIED="1518776355908" TEXT="Embedded methods try to combine the advantages of both previous methods. A learning algorithm takes advantage of its own variable selection process and performs feature selection and classification simultaneously.">
<node CREATED="1518776406863" ID="ID_228214122" MODIFIED="1518776407331" TEXT="Lasso regression performs L1 regularization which adds penalty equivalent to absolute value of the magnitude of coefficients."/>
<node CREATED="1518776510166" ID="ID_1816807238" MODIFIED="1518776512145" TEXT="Ridge regression performs L2 regularization which adds penalty equivalent to square of the magnitude of coefficients."/>
</node>
</node>
</node>
</node>
<node CREATED="1518763827730" ID="ID_152656594" MODIFIED="1518763839312" POSITION="right" TEXT="Feature Encoding">
<node CREATED="1518789897117" ID="ID_1096206099" MODIFIED="1518789900646" TEXT="Machine Learning algorithms perform Linear Algebra on Matrices, which means all features must be numeric. Encoding helps us do this."/>
<node CREATED="1518789948645" ID="ID_1342405774" MODIFIED="1518789949896" TEXT="Label Encoding">
<node CREATED="1518789979932" ID="ID_1895502527" MODIFIED="1518789981284" TEXT="One Hot Encoding">
<node CREATED="1518790000851" ID="ID_335754802" MODIFIED="1518790001679" TEXT="In One Hot Encoding, make sure the encodings are done in a way that all features are linearly independent."/>
</node>
</node>
</node>
<node CREATED="1518763855841" ID="ID_1734586861" MODIFIED="1518763857061" POSITION="right" TEXT="Feature Normalisation or Scaling">
<node CREATED="1518790038851" ID="ID_1763323339" MODIFIED="1518790040224" TEXT="Since the range of values of raw data varies widely, in some machine learning algorithms, objective functions will not work properly without normalization. Another reason why feature scaling is applied is that gradient descent converges much faster with feature scaling than without it."/>
<node CREATED="1518790081473" ID="ID_1433240108" MODIFIED="1518790082181" TEXT="Methods">
<node CREATED="1518790090601" ID="ID_367899702" MODIFIED="1518790091357" TEXT="Rescaling">
<node CREATED="1518790103323" ID="ID_92397996" MODIFIED="1518790103885" TEXT="The simplest method is rescaling the range of features to scale the range in [0, 1] or [&#x2212;1, 1]."/>
</node>
<node CREATED="1518790119665" ID="ID_1469917838" MODIFIED="1518790120429" TEXT="Standardization">
<node CREATED="1518790169472" ID="ID_1241442150" MODIFIED="1518790170807" TEXT="Feature standardization makes the values of each feature in the data have zero-mean (when subtracting the mean in the numerator) and unit-variance."/>
</node>
<node CREATED="1518790182311" ID="ID_1154996941" MODIFIED="1518790183027" TEXT="Scaling to unit length">
<node CREATED="1518790190231" ID="ID_1717257328" MODIFIED="1518790191378" TEXT="To scale the components of a feature vector such that the complete vector has length one."/>
</node>
</node>
</node>
<node CREATED="1518763881768" ID="ID_404144755" MODIFIED="1518763884141" POSITION="right" TEXT="Dataset Construction">
<node CREATED="1518790235486" ID="ID_841416201" MODIFIED="1518790320378" TEXT="Training Dataset">
<node CREATED="1518790252950" ID="ID_1825022323" MODIFIED="1518790253842" TEXT="A set of examples used for learning">
<node CREATED="1518790271085" ID="ID_362488943" MODIFIED="1518790272296" TEXT="To fit the parameters of the classifier in the Multilayer Perceptron, for instance, we would use the training set to find the &#x201c;optimal&#x201d; weights when using back-progapation."/>
</node>
</node>
<node CREATED="1518790326980" ID="ID_1067001938" MODIFIED="1518790327945" TEXT="Test Dataset">
<node CREATED="1518790347100" ID="ID_1617862129" MODIFIED="1518790347592" TEXT="A set of examples used only to assess the performance of a fully-trained classifier">
<node CREATED="1518790383035" ID="ID_1730164500" MODIFIED="1518790384255" TEXT="In the Multilayer Perceptron case, we would use the test to estimate the error rate after we have chosen the final model (MLP size and actual weights) After assessing the final model on the test set, YOU MUST NOT tune the model any further."/>
</node>
</node>
<node CREATED="1518790412003" ID="ID_529172700" MODIFIED="1518790412822" TEXT="Validation Dataset">
<node CREATED="1518790426482" ID="ID_1032128369" MODIFIED="1518790427142" TEXT="A set of examples used to tune the parameters of a classifier">
<node CREATED="1518790454721" ID="ID_49348310" MODIFIED="1518790457292" TEXT="In the Multilayer Perceptron case, we would use the validation set to find the &#x201c;optimal&#x201d; number of hidden units or determine a stopping point for the back-propagation algorithm"/>
</node>
</node>
<node CREATED="1518790496369" ID="ID_1036804930" MODIFIED="1518790498045" TEXT="Cross Validation">
<node CREATED="1518790512056" ID="ID_36291892" MODIFIED="1518790512668" TEXT="One round of cross-validation involves partitioning a sample of data into complementary subsets, performing the analysis on one subset (called the training set), and validating the analysis on the other subset (called the validation set or testing set). To reduce variability, multiple rounds of cross-validation are performed using different partitions, and the validation results are averaged over the rounds."/>
</node>
</node>
</node>
</map>
