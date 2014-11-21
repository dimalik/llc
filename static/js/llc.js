var normaliseArray = function(array) {
	var newArray = new Array();
	var i, j;
	for (i=0;i<array.length;i++){
		if (array[i] != 0) {
			for (j=0;j<array[i];j++) {
				newArray.push((i / 2));
			}
		}
	}
	return newArray;
}

var getMean = function(array) {
	var sum = 0;
	for (i=0;i<array.length;i++) {
		sum += array[i];
	}
	return (sum / array.length).toFixed(2);
}

var getSD = function(array) {
	var mean = getMean(array);
	var sum = 0, i = 0, sd;
	for (i=0; i<array.length;i++){
		sum += Math.pow((array[i] - mean), 2)
	}
	sd = Math.sqrt((1 / (array.length - 1)) * sum);
	return sd.toFixed(2);
}

function getMode(array)
{
    if (array.length == 0)
        return null;

    var modeMap = {},
        maxEl = array[0],
        maxCount = 1;

    for(var i = 0; i < array.length; i++)
    {
        var el = array[i];

        if (modeMap[el] == null)
            modeMap[el] = 1;
        else
            modeMap[el]++;

        if (modeMap[el] > maxCount)
        {
            maxEl = el;
            maxCount = modeMap[el];
        }
        else if (modeMap[el] == maxCount)
        {
            maxEl += '&' + el;
            maxCount = modeMap[el];
        }
    }
    return maxEl;
}

function getMedian(array) {

    array.sort( function(a,b) {return a - b;} );

    var half = Math.floor(array.length/2);

    if(array.length % 2)
        return array[half];
    else
        return (array[half-1] + array[half]) / 2.0;
}



var getScores = function() {
	var data = getRatingData();

	var before_scores = [];
	var after_scores = [];

	for (var i=0; i<data.length; i++) {
		before_scores.push(data[i]['before']);
		after_scores.push(data[i]['after']);
	}



	var normalised_before = normaliseArray(before_scores);
	var normalised_after = normaliseArray(after_scores);
	var normalised_overall = normalised_before.concat(normalised_after);
	
	$("#beforeMean").html(getMean(normalised_before));
	$("#afterMean").html(getMean(normalised_after));
	$("#beforeMode").html(getMode(normalised_before));
	$("#afterMode").html(getMode(normalised_after));
	$("#beforeMedian").html(getMedian(normalised_before));
	$("#afterMedian").html(getMedian(normalised_after));
	$("#beforeSD").html(getSD(normalised_before));
	$("#afterSD").html(getSD(normalised_after));
	if (getMean(normalised_overall) != "NaN") {
		$(".star-box-giga-star").html(getMean(normalised_overall));
	} else {
		$(".star-box-giga-star").html(getMean("NA"));
	}
	return data;
}

var makeChart = function() {
	var chart = c3.generate({
		bindto: '#chart',
	    data: {
			json: getScores(),
	        type: 'bar',
			keys: {
				x: 'pos',
				value: ['before', 'after'],
			}
	    },
	    bar: {
	        width: {
	            ratio: 0.9
	        }
	    },
		axis : {
		        y : {
		            tick: {
						fit: true,
						format: function (x) { if (x % 1 === 0) {return x;} }
		            },
					min: 1,
					max: 10
		        }
		    },
	    tooltip: {
	          format: {
	              title: function (d) { return 'Score: ' + d; }
	          }
	      },
		  color: {
			  pattern: ["#3E606F", "#91AA9D"]
		  }
	});
}