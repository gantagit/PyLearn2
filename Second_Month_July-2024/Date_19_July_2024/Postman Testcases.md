var jsResponse = pm.response.json();

pm.test("TC1 Status Code is 200", function() {
    pm.response.to.have.status(200);
});

pm.test("TC2 verify booking is created successfully", function(){
    pm.expect(jsResponse["bookingid"]).not.equal(null);
    pm.expect(jsResponse["booking"]["firstname"]).to.equal("Sally");


});

pm.test("TC3 verify booking is created successfully", function(){
    jsResponse["bookingid"] = null;
    jsResponse["booking"]["firstname"] = "VIJAY";

    pm.expect(jsResponse["bookingid"]).to.equal(null);
    pm.expect(jsResponse["booking"]["firstname"]).to.equal("Sally");
    PM.EXPECT(jsResponse["booking"]["Lastname"]).to.equal("Gan")
});

