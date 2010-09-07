function updateRows(rows) {
	var tbody = $('status').select('tbody').pop();
	var otr = tbody.select('tr');
	for(var i=0;i<otr.length;i++) {
		otr[i].remove();
	}	
	for(var i=0;i<rows.length;i++) {
		if (i % 2 == 0) {
			rows[i].addClassName('even');
		} else {
			rows[i].addClassName('odd');
		}
		tbody.appendChild(rows[i]);
	}
	
}

function updateStatus(resp) {
    if (resp.tamatar && resp.tamatar.length > 0) {
		var l = resp.tamatar.length;
		var trs = [];
		for (var i=0; i<l; i++) {
			var stat = resp.tamatar[i];
			var tr = new Element('tr', {})
			for (var j=0; j<stat.length; j++) {
				var td = new Element('td', {}).update(stat[j]);
				tr.appendChild(td);	
			}
			trs[i] = tr;
		}
		updateRows(trs);
	}
}

function resetForm() {
	form = $('commandform');
	var tinput = form['tamatar'];
	tinput.options.selectedIndex = 0;
	var cinput = form['mode'];
	cinput.options.selectedIndex = 0;	
	var info = $('resp');
	info.update('');
}


function submitCommand() {
	var form = $('commandform');
	var info = $('resp');	
	
	var tInput = form['tamatar'];
	if (!tInput) {
		return false;
	}

	var tVal = $F(tInput);
	if (tVal <= 0) {
		return false;
	} 

	var cInput = form['mode'];
	if (!cInput) {
		return false;
	}

	var cVal = $F(cInput);
	if (cVal == '') {
		return false;
	}
	
	info.update('sending ...');
	new Ajax.Request(
		'/sendcmd/?tamatar='+tVal+'&cmd='+cVal,
		{
			method: 'get',
			onSuccess: function(resp) {
				if (resp.responseJSON && resp.responseJSON.success == 1) {
					info.update('success!');	
				} else {
					info.update('failed!');
				}
				resetForm();	
			},
			onFailure: function(resp) {
				info.update('failed!');
				resetForm();	
			}
		}
		
	);


}


window.onload = function() {
    var p = new Ajax.PeriodicalUpdater('foo', '/status/',
	{
	    method: 'get',
	    frequency: 5,
	    onSuccess: function(r) {
		if (r.responseJSON) {
		    updateStatus(r.responseJSON);
		
		}
	    }	  
        }
    )	
}
