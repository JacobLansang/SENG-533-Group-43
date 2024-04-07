import json 
import random

# This script will create [numOwners] many owners, and create 5 petRecords for each owner
numOwners = 2000

owners = []
petrecords = []
clinics = [
{
    "ClinicID": 1,
    "Address": "3 Elmwood Ave",
    "NumberOfVets": 2
},
{ 
    "ClinicID": 2,
    "Address": "482 High Noon Avenue",
    "NumberOfVets": 7
},
{
    "ClinicID": 3,
    "Address": "6 East Marshall Dr",
    "NumberOfVets": 13
},
{
    "ClinicID": 4,
    "Address": "866 West Miller Street",
    "NumberOfVets": 4
},
{
    "ClinicID": 5,
    "Address": "825 Railroad Dr",
    "NumberOfVets": 6
}]

# 1000 popular surnames
surnames = [
"SMITH","JOHNSON","WILLIAMS","BROWN","JONES","MILLER","DAVIS","GARCIA","RODRIGUEZ","WILSON","MARTINEZ","ANDERSON","TAYLOR","THOMAS","HERNANDEZ","MOORE","MARTIN","JACKSON","THOMPSON","WHITE","LOPEZ","LEE","GONZALEZ","HARRIS","CLARK","LEWIS","ROBINSON","WALKER","PEREZ","HALL","YOUNG","ALLEN","SANCHEZ","WRIGHT","KING","SCOTT","GREEN","BAKER","ADAMS","NELSON","HILL","RAMIREZ","CAMPBELL","MITCHELL","ROBERTS","CARTER","PHILLIPS","EVANS","TURNER","TORRES","PARKER","COLLINS","EDWARDS","STEWART","FLORES","MORRIS","NGUYEN","MURPHY","RIVERA","COOK","ROGERS","MORGAN","PETERSON","COOPER","REED","BAILEY","BELL","GOMEZ","KELLY","HOWARD","WARD","COX","DIAZ","RICHARDSON","WOOD","WATSON","BROOKS","BENNETT","GRAY","JAMES","REYES","CRUZ","HUGHES","PRICE","MYERS","LONG","FOSTER","SANDERS","ROSS","MORALES","POWELL","SULLIVAN","RUSSELL","ORTIZ","JENKINS","GUTIERREZ","PERRY","BUTLER","BARNES","FISHER","HENDERSON","COLEMAN","SIMMONS","PATTERSON","JORDAN","REYNOLDS","HAMILTON","GRAHAM","KIM","GONZALES","ALEXANDER","RAMOS","WALLACE","GRIFFIN","WEST","COLE","HAYES","CHAVEZ","GIBSON","BRYANT","ELLIS","STEVENS","MURRAY",
"FORD","MARSHALL","OWENS","MCDONALD","HARRISON","RUIZ","KENNEDY","WELLS","ALVAREZ","WOODS","MENDOZA","CASTILLO","OLSON","WEBB","WASHINGTON","TUCKER","FREEMAN","BURNS","HENRY","VASQUEZ","SNYDER","SIMPSON","CRAWFORD","JIMENEZ","PORTER","MASON","SHAW","GORDON","WAGNER","HUNTER","ROMERO","HICKS","DIXON","HUNT","PALMER","ROBERTSON","BLACK","HOLMES","STONE","MEYER","BOYD","MILLS","WARREN","FOX","ROSE","RICE","MORENO","SCHMIDT","PATEL","FERGUSON","NICHOLS","HERRERA","MEDINA","RYAN","FERNANDEZ","WEAVER","DANIELS","STEPHENS","GARDNER","PAYNE","KELLEY","DUNN","PIERCE","ARNOLD","TRAN","SPENCER","PETERS","HAWKINS","GRANT","HANSEN","CASTRO","HOFFMAN","HART","ELLIOTT","CUNNINGHAM","KNIGHT","BRADLEY","CARROLL","HUDSON","DUNCAN","ARMSTRONG","BERRY","ANDREWS","JOHNSTON","RAY","LANE","RILEY","CARPENTER","PERKINS","AGUILAR","SILVA","RICHARDS","WILLIS","MATTHEWS","CHAPMAN","LAWRENCE","GARZA","VARGAS","WATKINS","WHEELER","LARSON","CARLSON","HARPER","GEORGE","GREENE","BURKE","GUZMAN","MORRISON","MUNOZ","JACOBS","OBRIEN","LAWSON","FRANKLIN","LYNCH","BISHOP","CARR","SALAZAR","AUSTIN","MENDEZ","GILBERT","JENSEN",
"WILLIAMSON","MONTGOMERY","HARVEY","OLIVER","HOWELL","DEAN","HANSON","WEBER","GARRETT","SIMS","BURTON","FULLER","SOTO","MCCOY","WELCH","CHEN","SCHULTZ","WALTERS","REID","FIELDS","WALSH","LITTLE","FOWLER","BOWMAN","DAVIDSON","MAY","DAY","SCHNEIDER","NEWMAN","BREWER","LUCAS","HOLLAND","WONG","BANKS","SANTOS","CURTIS","PEARSON","DELGADO","VALDEZ","PENA","RIOS","DOUGLAS","SANDOVAL","BARRETT","HOPKINS","KELLER","GUERRERO","STANLEY","BATES","ALVARADO","BECK","ORTEGA","WADE","ESTRADA","CONTRERAS","BARNETT","CALDWELL","SANTIAGO","LAMBERT","POWERS","CHAMBERS","NUNEZ","CRAIG","LEONARD","LOWE","RHODES","BYRD","GREGORY","SHELTON","FRAZIER","BECKER","MALDONADO","FLEMING","VEGA","SUTTON","COHEN","JENNINGS","PARKS","MCDANIEL","WATTS","BARKER","NORRIS","VAUGHN","VAZQUEZ","HOLT","SCHWARTZ","STEELE","BENSON","NEAL","DOMINGUEZ","HORTON","TERRY","WOLFE","HALE","LYONS","GRAVES","HAYNES","MILES","PARK","WARNER","PADILLA","BUSH","THORNTON","MCCARTHY","MANN","ZIMMERMAN","ERICKSON","FLETCHER","MCKINNEY","PAGE","DAWSON","JOSEPH","MARQUEZ","REEVES","KLEIN","ESPINOZA","BALDWIN","MORAN","LOVE","ROBBINS","HIGGINS","BALL",
"CORTEZ","LE","GRIFFITH","BOWEN","SHARP","CUMMINGS","RAMSEY","HARDY","SWANSON","BARBER","ACOSTA","LUNA","CHANDLER","BLAIR","DANIEL","CROSS","SIMON","DENNIS","OCONNOR","QUINN","GROSS","NAVARRO","MOSS","FITZGERALD","DOYLE","MCLAUGHLIN","ROJAS","RODGERS","STEVENSON","SINGH","YANG","FIGUEROA","HARMON","NEWTON","PAUL","MANNING","GARNER","MCGEE","REESE","FRANCIS","BURGESS","ADKINS","GOODMAN","CURRY","BRADY","CHRISTENSEN","POTTER","WALTON","GOODWIN","MULLINS","MOLINA","WEBSTER","FISCHER","CAMPOS","AVILA","SHERMAN","TODD","CHANG","BLAKE","MALONE","WOLF","HODGES","JUAREZ","GILL","FARMER","HINES","GALLAGHER","DURAN","HUBBARD","CANNON","MIRANDA","WANG","SAUNDERS","TATE","MACK","HAMMOND","CARRILLO","TOWNSEND","WISE","INGRAM","BARTON","MEJIA","AYALA","SCHROEDER","HAMPTON","ROWE","PARSONS","FRANK","WATERS","STRICKLAND","OSBORNE","MAXWELL","CHAN","DELEON","NORMAN","HARRINGTON","CASEY","PATTON","LOGAN","BOWERS","MUELLER","GLOVER","FLOYD","HARTMAN","BUCHANAN","COBB","FRENCH","KRAMER","MCCORMICK","CLARKE","TYLER","GIBBS","MOODY","CONNER","SPARKS","MCGUIRE","LEON","BAUER","NORTON","POPE","FLYNN","HOGAN","ROBLES",
"SALINAS","YATES","LINDSEY","LLOYD","MARSH","MCBRIDE","OWEN","SOLIS","PHAM","LANG","PRATT","LARA","BROCK","BALLARD","TRUJILLO","SHAFFER","DRAKE","ROMAN","AGUIRRE","MORTON","STOKES","LAMB","PACHECO","PATRICK","COCHRAN","SHEPHERD","CAIN","BURNETT","HESS","LI","CERVANTES","OLSEN","BRIGGS","OCHOA","CABRERA","VELASQUEZ","MONTOYA","ROTH","MEYERS","CARDENAS","FUENTES","WEISS","HOOVER","WILKINS","NICHOLSON","UNDERWOOD","SHORT","CARSON","MORROW","COLON","HOLLOWAY","SUMMERS","BRYAN","PETERSEN","MCKENZIE","SERRANO","WILCOX","CAREY","CLAYTON","POOLE","CALDERON","GALLEGOS","GREER","RIVAS","GUERRA","DECKER","COLLIER","WALL","WHITAKER","BASS","FLOWERS","DAVENPORT","CONLEY","HOUSTON","HUFF","COPELAND","HOOD","MONROE","MASSEY","ROBERSON","COMBS","FRANCO","LARSEN","PITTMAN","RANDALL","SKINNER","WILKINSON","KIRBY","CAMERON","BRIDGES","ANTHONY","RICHARD","KIRK","BRUCE","SINGLETON","MATHIS","BRADFORD","BOONE","ABBOTT","CHARLES","ALLISON","SWEENEY","ATKINSON","HORN","JEFFERSON","ROSALES","YORK","CHRISTIAN","PHELPS","FARRELL","CASTANEDA","NASH","DICKERSON","BOND","WYATT","FOLEY","CHASE","GATES","VINCENT","MATHEWS",
"HODGE","GARRISON","TREVINO","VILLARREAL","HEATH","DALTON","VALENCIA","CALLAHAN","HENSLEY","ATKINS","HUFFMAN","ROY","BOYER","SHIELDS","LIN","HANCOCK","GRIMES","GLENN","CLINE","DELACRUZ","CAMACHO","DILLON","PARRISH","ONEILL","MELTON","BOOTH","KANE","BERG","HARRELL","PITTS","SAVAGE","WIGGINS","BRENNAN","SALAS","MARKS","RUSSO","SAWYER","BAXTER","GOLDEN","HUTCHINSON","LIU","WALTER","MCDOWELL","WILEY","RICH","HUMPHREY","JOHNS","KOCH","SUAREZ","HOBBS","BEARD","GILMORE","IBARRA","KEITH","MACIAS","KHAN","ANDRADE","WARE","STEPHENSON","HENSON","WILKERSON","DYER","MCCLURE","BLACKWELL","MERCADO","TANNER","EATON","CLAY","BARRON","BEASLEY","ONEAL","PRESTON","SMALL","WU","ZAMORA","MACDONALD","VANCE","SNOW","MCCLAIN","STAFFORD","OROZCO","BARRY","ENGLISH","SHANNON","KLINE","JACOBSON","WOODARD","HUANG","KEMP","MOSLEY","PRINCE","MERRITT","HURST","VILLANUEVA","ROACH","NOLAN","LAM","YODER","MCCULLOUGH","LESTER","SANTANA","VALENZUELA","WINTERS","BARRERA","LEACH","ORR","BERGER","MCKEE","STRONG","CONWAY","STEIN","WHITEHEAD","BULLOCK","ESCOBAR","KNOX","MEADOWS","SOLOMON","VELEZ","ODONNELL","KERR","STOUT","BLANKENSHIP",
"BROWNING","KENT","LOZANO","BARTLETT","PRUITT","BUCK","BARR","GAINES","DURHAM","GENTRY","MCINTYRE","SLOAN","MELENDEZ","ROCHA","HERMAN","SEXTON","MOON","HENDRICKS","RANGEL","STARK","LOWERY","HARDIN","HULL","SELLERS","ELLISON","CALHOUN","GILLESPIE","MORA","KNAPP","MCCALL","MORSE","DORSEY","WEEKS","NIELSEN","LIVINGSTON","LEBLANC","MCLEAN","BRADSHAW","GLASS","MIDDLETON","BUCKLEY","SCHAEFER","FROST","HOWE","HOUSE","MCINTOSH","HO","PENNINGTON","REILLY","HEBERT","MCFARLAND","HICKMAN","NOBLE","SPEARS","CONRAD","ARIAS","GALVAN","VELAZQUEZ","HUYNH","FREDERICK","RANDOLPH","CANTU","FITZPATRICK","MAHONEY","PECK","VILLA","MICHAEL","DONOVAN","MCCONNELL","WALLS","BOYLE","MAYER","ZUNIGA","GILES","PINEDA","PACE","HURLEY","MAYS","MCMILLAN","CROSBY","AYERS","CASE","BENTLEY","SHEPARD","EVERETT","PUGH","DAVID","MCMAHON","DUNLAP","BENDER","HAHN","HARDING","ACEVEDO","RAYMOND","BLACKBURN","DUFFY","LANDRY","DOUGHERTY","BAUTISTA","SHAH","POTTS","ARROYO","VALENTINE","MEZA","GOULD","VAUGHAN","FRY","RUSH","AVERY","HERRING","DODSON","CLEMENTS","SAMPSON","TAPIA","BEAN","LYNN","CRANE","FARLEY","CISNEROS","BENTON","ASHLEY",
"MCKAY","FINLEY","BEST","BLEVINS","FRIEDMAN","MOSES","SOSA","BLANCHARD","HUBER","FRYE","KRUEGER","BERNARD","ROSARIO","RUBIO","MULLEN","BENJAMIN","HALEY","CHUNG","MOYER","CHOI","HORNE","YU","WOODWARD","ALI","NIXON","HAYDEN","RIVERS","ESTES","MCCARTY","RICHMOND","STUART","MAYNARD","BRANDT","OCONNELL","HANNA","SANFORD","SHEPPARD","CHURCH","BURCH","LEVY","RASMUSSEN","COFFEY","PONCE","FAULKNER","DONALDSON","SCHMITT","NOVAK","COSTA","MONTES","BOOKER","CORDOVA","WALLER","ARELLANO","MADDOX","MATA","BONILLA","STANTON","COMPTON","KAUFMAN","DUDLEY","MCPHERSON","BELTRAN","DICKSON","MCCANN","VILLEGAS","PROCTOR","HESTER","CANTRELL","DAUGHERTY","CHERRY","BRAY","DAVILA","ROWLAND","LEVINE","MADDEN","SPENCE","GOOD", "IRWIN", "WERNER", "KRAUSE", "PETTY", "WHITNEY", "BAIRD", "HOOPER", "POLLARD", "ZAVALA", "JARVIS", "HOLDEN", "HAAS", "HENDRIX", "MCGRATH", "BIRD", "LUCERO", "TERRELL", "RIGGS", "JOYCE", "MERCER", "ROLLINS", "GALLOWAY", "DUKE", "ODOM", "ANDERSEN", "DOWNS", "HATFIELD", "BENITEZ", "ARCHER", "HUERTA", "TRAVIS", "MCNEIL", "HINTON", "ZHANG", "HAYS", "MAYO", "FRITZ", "BRANCH", "MOONEY", "EWING", "RITTER", 
"ESPARZA", "FREY", "BRAUN", "GAY", "RIDDLE", "HANEY", "KAISER", "HOLDER", "CHANEY", "MCKNIGHT", "GAMBLE", "VANG", "COOLEY", "CARNEY", "COWAN", "FORBES", "FERRELL", "DAVIES", "BARAJAS", "SHEA", "OSBORN", "BRIGHT", "CUEVAS", "BOLTON", "MURILLO", "LUTZ", "DUARTE", "KIDD", "KEY", "COOKE"
]

# 236 popular pet names
petnames = [
"Bullet","Bullwinkle","Bully","Bumper","Bunky","Buster","Buster-brown","Butch","Butchy","Caesar","Calvin","Capone","Captain","Chad","Chamberlain","Champ","Chance","Charles",
"Charlie","Charlie Brown","Charmer","Chase","Chauncey","Chaz","Checkers","Chester","Chevy","Chewie","Chewy","Chico","Chief","Chili","China","Chip","Chipper","Chippy","Chips",
"Chubbs","Chucky","Chyna","Cinder","Cindy","Clancy","Cleo","Cleopatra","Clicker","Clifford","Clover","Clyde","Coal","Cobweb","Coco","Cocoa","Cole","Comet","Commando","Conan",
"Connor","Cookie","Cooper","Copper","Corky","Cosmo","Cotton","Cozmo","Crackers","Cricket","Crystal","Cubby","Cubs","Cujo","Cupcake","Curly","Curry","Cutie","Cutie-pie","Cyrus",
"Daffy","Daisey-mae","Daisy","Dakota","Dallas","Dandy","Dante","Daphne","Darby","Darcy","Darwin","Dash","Dave","Deacon","Dee","Dee Dee","Dempsey","Destini","Dewey","Dexter",
"Dharma","Diamond","Dickens","Diego","Diesel","Digger","Dillon","Dinky","Dino","Diva","Dixie","Dobie","Doc","Dodger","Doggon","Dolly","Domino","Doodles","Doogie","Dots","Dottie",
"Dozer","Dragster","Dreamer","Duchess","Dude","Dudley","Duffy","Duke","Duncan","Dunn","Dusty","Dutches","Dutchess","Dylan","Earl","Ebony","Echo","Eddie","Eddy","Edgar","Edsel",
"Eifel","Einstein","Ellie","Elliot","Elmo","Elvis","Elwood","Ember","Emily","Emma","Emmy","Erin","Ernie","Eva","Faith","Fancy","Felix","Fergie","Ferris","Fido","Fifi","Figaro",
"Finnegan","Fiona","Flake","Flakey","Flash","Flint","Flopsy","Flower","Floyd","Fluffy","Fonzie","Foxy","Francais","Frankie","Franky","Freckles","Fred","Freddie","Freddy","Freedom",
"Freeway","Fresier","Friday","Frisco","Frisky","Fritz","Frodo","Frosty","Furball","Fuzzy","Gabby","Gabriella","Garfield","Gasby","Gator","Gavin","Genie","George","Georgia","Georgie",
"Giant","Gibson","Gidget","Gigi","Gilbert","Gilda","Ginger","Ginny","Girl","Gizmo","Godiva","Goldie","Goober","Goose","Gordon","Grace","Grace","Gracie","Gracie","Grady","Greenie",
"Greta","Gretchen","Gretel","Gretta","Griffen","Gringo","Grizzly","Gromit","Grover","Gucci","Guido","Guinness","Gunner","Gunther"
]

# 16 types of pets (cat and dog repeated for popularity)
animals = [
    "Cat","Cat","Cat","Dog","Dog","Dog","Rabbit","Ferret","Hamster","Guinea Pig","Bird","Reptile","Amphibian","Snail", "Rat", "Hedgehog"
]

# counter used for petrecord ID
records = 0

# loop to create all owner records
for O in range(numOwners):
    owner = {
        "OwnerID": 1,
        "Surname": "name",
        "TotalFeesPaid": 100 
    }
    owner["OwnerID"] = O+1
    owner["Surname"] = surnames[O%1000]
    owner["TotalFeesPaid"] = random.randint(0, 1000)
    owners.append(owner)
    
    # loop to create 5 petRecords for each owner
    for P in range (5):
        records += 1
        petrecord = {
            "PetID": 1,
            "ClinicID": 1,
            "OwnerID": 1,
            "Animal":"cat",
            "Name":"bob",
            "Age":10,
            "SpayedOrNeutered": "No"
        }
        petrecord["PetID"] = records
        petrecord["ClinicID"] = random.randint(1, 5)
        petrecord["OwnerID"] = owner["OwnerID"]
        petrecord["Animal"] = animals[random.randint(0, 15)]
        petrecord["Name"] = petnames[random.randint(0, 235)]
        petrecord["Age"] = random.randint(1, 15)
        petrecord["SpayedOrNeutered"] = "Yes" if random.randint(0, 1) else "No"
        petrecords.append(petrecord)

# export as json files
clinicsJSON = json.dumps(clinics)
ownersJSON = json.dumps(owners)
petrecordsJSON = json.dumps(petrecords)
with open('clinics.json', 'w', encoding='utf-8') as f:
    json.dump(clinics, f, ensure_ascii=False, indent=4)
with open('owners.json', 'w', encoding='utf-8') as f:
    json.dump(owners, f, ensure_ascii=False, indent=4)
with open('petrecords.json', 'w', encoding='utf-8') as f:
    json.dump(petrecords, f, ensure_ascii=False, indent=4)