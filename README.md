<h1>Uploadzzer</h1>
<div>This is a Python program that performs web requests to an uploader, fuzzing the various extensions and formats of the files to find any vulnerabilities in the upload management.</div>
<h2>Requirements</h2>
<div>In order to run this program, you will need the following libraries:</div>
<ol>
<li></div>requests</li>
<li>argparse</li>
</ol>
<div>You can install them using pip:</div>
<pre>pip install -r requirements.txt</pre>
<h2>Usage</h2>
<div>To use this program, simply run the following command:</div>
<pre><span>python3 uploadzzer.py -u &lt;url&gt; -f &lt;path/to/file&gt; -e &lt;error in response&gt; --permitted &lt;formats&gt;</span></pre>
<div>Where:</div>
<ol>
<li><code>&lt;url&gt;</code> is the URL of the uploader</li>
<li><code>&lt;path&gt;</code> is the path to the file that will be uploaded</li>
<li><code>&lt;error in response&gt;</code> is the discriminator used to filter error and successfull responses</li>
<li><code>&lt;permitted&gt;</code> is a space-separated list of formats to be fuzzed (e.g. <code>jpg png gif</code>)</li>
</ol>
This is just an example pls refer to help for a complete guide. <br>
You can use <code>python3 uploadzzer -h </code> for a complete man page about the methods implemented.

<h2>Acknowledgements</h2>
<div>The methods implemented in this program were based on the following <a href="https://book.hacktricks.xyz/pentesting-web/file-upload">guide</a>.</div>
