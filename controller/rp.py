from flask import Blueprint, render_template, request, redirect, url_for

from module.rp import RP

rp = Blueprint('rp', __name__)

@rp.route('/add-rp-stu/', methods=['GET', 'POST'])
def add_rp_stu():
    if request.method == 'GET':
        return render_template('add_rp_stu.html')
    else:
        sno = request.form.get('sno')
        rpname = request.form.get('rpname')
        rpgrade = request.form.get('rpgrade')
        rptype = request.values.get('rptype')
        rpdate = request.form.get('rpdate')
        anote = request.form.get('anote')
        rpdate.replace('/', '-')
        rp = RP()
        rp.Add_RP(sno, rpname, rptype, rpgrade, rpdate, anote)
        return redirect('/stu-rp-list/')

@rp.route('/del-rp/<rpid>')
def del_course(rpid):
    rp = RP()
    result = rp.find_by_rpid(rpid)
    if result:
        rp.Delete_by_rpid(rpid)
        return redirect('/stu-rp-list/')
    else:
        return 'del-fail'


@rp.route('/rp-list/<rpid>')
def rp_list_rpid(rpid):
    rp = RP()
    result = rp.find_by_rpid(rpid)
    print(result)
    return render_template('update_rp.html', result=result)


@rp.route('/edit-rp/', methods=['POST'])
def editrp():
    rp = RP()
    rpid = request.form.get('rpid')
    rptype = request.values.get('rptype')
    rpname = request.form.get('rpname')
    sno = request.form.get('sno')
    rpgrade = request.form.get('rpgrade')
    rpdate = request.form.get('rpdate')
    anote = request.form.get('anote')
    if rpid:
        rp.update_rp(rpid, sno, rpname, rptype, rpgrade, rpdate, anote)
        return redirect('/stu-rp-list/')
    else:
        return 'edit-fail'
