// Auto-generated. Do not edit!

// (in-package exploration_manager.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class PairOpt {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.from_drone_id = null;
      this.to_drone_id = null;
      this.stamp = null;
      this.ego_ids = null;
      this.other_ids = null;
    }
    else {
      if (initObj.hasOwnProperty('from_drone_id')) {
        this.from_drone_id = initObj.from_drone_id
      }
      else {
        this.from_drone_id = 0;
      }
      if (initObj.hasOwnProperty('to_drone_id')) {
        this.to_drone_id = initObj.to_drone_id
      }
      else {
        this.to_drone_id = 0;
      }
      if (initObj.hasOwnProperty('stamp')) {
        this.stamp = initObj.stamp
      }
      else {
        this.stamp = 0.0;
      }
      if (initObj.hasOwnProperty('ego_ids')) {
        this.ego_ids = initObj.ego_ids
      }
      else {
        this.ego_ids = [];
      }
      if (initObj.hasOwnProperty('other_ids')) {
        this.other_ids = initObj.other_ids
      }
      else {
        this.other_ids = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PairOpt
    // Serialize message field [from_drone_id]
    bufferOffset = _serializer.int32(obj.from_drone_id, buffer, bufferOffset);
    // Serialize message field [to_drone_id]
    bufferOffset = _serializer.int32(obj.to_drone_id, buffer, bufferOffset);
    // Serialize message field [stamp]
    bufferOffset = _serializer.float64(obj.stamp, buffer, bufferOffset);
    // Serialize message field [ego_ids]
    bufferOffset = _arraySerializer.int8(obj.ego_ids, buffer, bufferOffset, null);
    // Serialize message field [other_ids]
    bufferOffset = _arraySerializer.int8(obj.other_ids, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PairOpt
    let len;
    let data = new PairOpt(null);
    // Deserialize message field [from_drone_id]
    data.from_drone_id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [to_drone_id]
    data.to_drone_id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [stamp]
    data.stamp = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ego_ids]
    data.ego_ids = _arrayDeserializer.int8(buffer, bufferOffset, null)
    // Deserialize message field [other_ids]
    data.other_ids = _arrayDeserializer.int8(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.ego_ids.length;
    length += object.other_ids.length;
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'exploration_manager/PairOpt';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f1b382d48f9c952cdea39f0f21949ad6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    int32 from_drone_id
    int32 to_drone_id
    
    float64 stamp
    int8[] ego_ids
    int8[] other_ids
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PairOpt(null);
    if (msg.from_drone_id !== undefined) {
      resolved.from_drone_id = msg.from_drone_id;
    }
    else {
      resolved.from_drone_id = 0
    }

    if (msg.to_drone_id !== undefined) {
      resolved.to_drone_id = msg.to_drone_id;
    }
    else {
      resolved.to_drone_id = 0
    }

    if (msg.stamp !== undefined) {
      resolved.stamp = msg.stamp;
    }
    else {
      resolved.stamp = 0.0
    }

    if (msg.ego_ids !== undefined) {
      resolved.ego_ids = msg.ego_ids;
    }
    else {
      resolved.ego_ids = []
    }

    if (msg.other_ids !== undefined) {
      resolved.other_ids = msg.other_ids;
    }
    else {
      resolved.other_ids = []
    }

    return resolved;
    }
};

module.exports = PairOpt;
