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
