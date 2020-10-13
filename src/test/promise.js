'use strict';
const buildType = process.config.target_defaults.default_configuration;
const assert = require('assert');
const common = require('./common');

module.exports = test(require(`./build/${buildType}/binding.node`))
  .then(() => test(require(`./build/${buildType}/binding_noexcept.node`)));

async function test(binding) {
  assert.strictEqual(binding.promise.isPromise({}), false);

  const resolving = binding.promise.resolvePromise('resolved');
  await assert.strictEqual(binding.promise.isPromise(resolving), true);
  resolving.then(common.mustCall()).catch(common.mustNotCall());

  const rejecting = binding.promise.rejectPromise('error');
  await assert.strictEqual(binding.promise.isPromise(rejecting), true);
  rejecting.then(common.mustNotCall()).catch(common.mustCall());
}
