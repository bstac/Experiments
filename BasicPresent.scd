//this is for the dome, 5 speakers
//evaluate with control + return
//or command + return on a mac

//this is code for starting the sever,viewing the local address,
//and changing input or output settings
NetAddr.localAddr; //view the local address
o = Server.local.options; //this makes it easier to type other commands
//below lines are for changing input and output settings
o.inDevice = "Built-in Microph"
o.inDevice = "MOTU UltraLite mk3 Hybrid";
o.outDevice = "MOTU UltraLite mk3 Hybrid";
o.outDevice = "Built-in Output"
//for the server
s.meter;//show the 'mixer'
s.reboot;//restart
s.boot;//use this to start
s.quit;//use this to end


//#1, evaluate first
//definition of my synth
(
SynthDef(\pitchFollow,{
	arg amp1=1, amp2=1, amp3=1, amp4=1, amp5=1, revb=1; //arguments
    var in, amp, freq, hasFreq, out; //variables
    in = Mix.new(SoundIn.ar([0,1])); //get a line in, two channels
    amp = Amplitude.kr(in, 0.05, 0.05); //amplitude of the line,
	//the above line is very imortant, without it the synth will play constantly
	//you dont want that, it is so painful
    # freq, hasFreq = Pitch.kr(in, ampThreshold: 0.02, median: 7);//pitch of the line
    out = SinOsc.ar(freq, 0, amp);//sine wave at the frequency and amplitude of the line
	out = FreeVerb.ar(out, revb/100, 0.5, 0.5, [amp1,amp2,amp3,amp4,amp5], 0);//reverb
	//the above line is where we expand to 5 channels, notice the array filled
	//with arguments, this is what is changed in the cube listener by processing's
	//messages. SC expands automatically this way, very convenient.
    Out.ar(0,out)
}).add;//store this definition, somwhere, so the computer can create this type of synth
)

//#2, evaluate second
//create and play a synth, store as x so we can refer to it
x = Synth.new(\pitchFollow);

//#3, evaluate third
//this listens for messages sent from processing using OSC
(
OSCdef('cubeListener',
	{
		arg msg;
		x.set(\revb, (msg[1])); //radius value, distance from center
		x.set(\amp1, (msg[2])); //these are for each speakers volume
		x.set(\amp2, (msg[3]));
		x.set(\amp3, (msg[4]));
		x.set(\amp4, (msg[5]));
		x.set(\amp5, (msg[6]));
	},
	"/cube"); //this means, look for messages with this name
//I beleive this is msg[0] by default, youll notice a
//correspondence in the processing code
)
//you are ready to run processing,
//if it is already started then you should be completely set up

//example of how to set an argment while a synth is playing
//you can do that manually
x.set(\revb, 20);



